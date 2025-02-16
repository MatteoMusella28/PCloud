#Importazione delle librerie
from flask import Flask,request,redirect,url_for
import json
import numpy as np
import joblib

#Creazione dell'app Flask
app = Flask(__name__)

#Database e modello di machine learning
db = {}
model = joblib.load('./server/model/model.pkl')
scaler = joblib.load('./server/model/scaler.pkl')

#Rotta per visualizzare il grafico
@app.route('/graph', methods=['GET'])
def graph():
    return redirect(url_for('static', filename='graph.html'))

#Rotta per ottenere l'elenco dei sensori
@app.route('/sensors',methods=['GET'])
def sensors():
    return json.dumps(list(db.keys())), 200

#Rotta per aggiungere dati di un sensore
@app.route('/sensors/<s>',methods=['POST'])
def add_data(s):
    data = request.values['data']
    val = float(request.values['val'])
    scaled_val = scaler.transform([[val]])
    prediction = model.predict(scaled_val)[-1]
    # prediction = model.predict_proba([[val]])[:,1][-1] > 0.1
    print(f'Prediction: {prediction}')
    if s in db:
        db[s].append((data, val, int(prediction)))
    else:
        db[s] = [(data, val, int(prediction))]
    return 'ok',200

#Rotta per ottenere i dati di un sensore
@app.route('/sensors/<s>',methods=['GET'])
def get_data(s):
    if s in db:
        r = []
        for i in range(len(db[s])):
            r.append([str(db[s][i][0]), db[s][i][1], db[s][i][2]])
        return json.dumps(r),200
    else:
        return 'sensor not found',404

# Rotta per calcolare l'umidità media del suolo (KPI n°1)
@app.route('/sensors/<s>/meansoil', methods=['GET'])
def get_mean_soil_moisture(s):
    if s in db:
        soil_moistures = [entry[1] for entry in db[s]]
        mean_moisture = np.mean(soil_moistures).round(2)
        return json.dumps([mean_moisture]), 200
    else:
        return 'sensor not found', 404

# Rotta per calcolare il totale del volume d'acqua utilizzata (KPI n°2)
@app.route('/sensors/<s>/totalwater', methods=['GET'])
def get_total_water(s):
    if s in db:
        total_water = sum([entry[1] for entry in db[s]])
        total_water = round(total_water, 2)  # Arrotonda a 2 cifre decimali
        return json.dumps([total_water]), 200
    else:
        return 'sensor not found', 404

# Rotta per calcolare la durata media di apertura della valvola (KPI n°3)
@app.route('/sensors/<s>/meantimevalve', methods=['GET'])
def get_mean_time_valve(s):
    if s in db:
        valve_open_times = [entry[2] for entry in db[s] if entry[2] == 1]  #Si assume che 1 vuol dire valvola aperta
        mean_time = np.mean(valve_open_times).round(2) if valve_open_times else 0
        return json.dumps([mean_time]), 200
    else:
        return 'sensor not found', 404

# Rotta per calcolare la frequenza di apertura della valvola (KPI n°4)
@app.route('/sensors/<s>/valvefrequency', methods=['GET'])
def get_valve_frequency(s):
    if s in db:
        frequency = sum([entry[2] for entry in db[s]])  #Conta quante volte la valvola si apre
        return json.dumps([frequency]), 200
    else:
        return 'sensor not found', 404

# Rotta per calcolare l'efficienza dell'uso dell'acqua (KPI n°5)
@app.route('/sensors/<s>/waterefficiency', methods=['GET'])
def get_water_efficiency(s):
    if s in db:
        total_water = sum([entry[1] for entry in db[s]])
        soil_moistures = [entry[1] for entry in db[s]]
        mean_moisture = np.mean(soil_moistures).round(2)
        water_efficiency = ((mean_moisture / total_water if total_water != 0 else 0)*100).round(2)
        # Aggiunta del simbolo di percentuale
        water_efficiency_with_symbol = f"{water_efficiency}%"
        return json.dumps([water_efficiency_with_symbol]), 200
    else:
        return 'sensor not found', 404

# Rotta per calcolare la variazione temporale dell'umidità del terreno (KPI n°6)
@app.route('/sensors/<s>/moisturevariation', methods=['GET'])
def get_moisture_variation(s):
    if s in db:
        moisture_values = [entry[1] for entry in db[s]]
        variation = np.std(moisture_values).round(2)  #Deviazione standard per mostrare la variazione
        return json.dumps([variation]), 200
    else:
        return 'sensor not found', 404

#Rotta per la homepage
@app.route('/', methods=['GET'])
def main():
    return redirect(url_for('static', filename='home.html'))
    # return os.getcwd()

#Esecuzione dell'app Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)