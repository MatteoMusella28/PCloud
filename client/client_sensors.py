#Importazione delle librerie
from requests import get, post
import time
import pandas as pd
import os

#Definizione di variabili
base_url = 'http://localhost:80'
sensor = 's1'

#Caricamento dei dati dal CSV
dfm = pd.read_csv('./client/csv/D_moisture.txt')
dfm["time_stamp"] = pd.to_datetime(dfm["time_stamp"], format='%d-%b-%Y %H:%M:%S')

#Ciclo per inviare i dati al server
for index, row in dfm.iterrows():
    data, val = row['time_stamp'], row['moisture']
    print(data,val)
    r = post(f'{base_url}/sensors/{sensor}', data={'data':data,'val':val})
    time.sleep(1)

#Messaggio finale
print('done')