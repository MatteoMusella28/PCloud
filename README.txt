Esame di Pervasive Computing e Servizi Cloud - Gestione di un Sistema di Irrigazione

Questo repository è il risultato del progetto per l’esame di Pervasive Computing e Servizi Cloud. 
L’obiettivo del progetto è sviluppare un sistema di analisi dei dati per la gestione di un sistema di irrigazione basato su tecnologie 
di machine learning e servizi cloud. Il sistema è costruito utilizzando il dataset fornito al seguente link:
https://data.mendeley.com/datasets/cjb4vy4mzj/3

Il progetto simula l'arrivo di dati in tempo reale e l'elaborazione di questi tramite un software di controllo che gira nel cloud, 
con il fine di ottimizzare la gestione dell'irrigazione in base alla condizione del terreno.

Obiettivo del Sistema
Il sistema è stato progettato per gestire un sistema di irrigazione basato sui dati di umidità del terreno (D_moisture). L'analisi di 
questi dati permette di prendere decisioni in tempo reale riguardo l'apertura o chiusura della valvola di irrigazione (D_valve), 
ottimizzando così il consumo d'acqua e migliorando l'efficienza del sistema di irrigazione. Il flusso di dati e la comunicazione tra i 
vari componenti avviene tramite HTTP e i dati vengono archiviati in un database.

Caratteristiche del Sistema:
1. Modello di Machine Learning (ML)
    Un modello di machine learning è stato sviluppato per prevedere se aprire la valvola di irrigazione (D_valve) in base ai dati di umidità 
    del terreno (D_moisture). Il modello è addestrato utilizzando i dati storici del dataset, per poi essere utilizzato in tempo reale per 
    prendere decisioni sull'irrigazione.
2. Client per la Lettura dei Dati
    Il sistema include un client che legge i dati relativi all'umidità del terreno in tempo reale. Il client invia i dati al server attraverso 
    richieste HTTP, uno alla volta, simulando così l’arrivo continuo di informazioni. Questo flusso continuo di dati è un aspetto fondamentale 
    per simulare l'operatività di un sistema di irrigazione in un ambiente reale.
3. Server per la Gestione e Analisi dei Dati
    Il server riceve i dati inviati dal client, li salva in un database per una successiva analisi e applica il modello di machine learning per 
    prendere la decisione se aprire o meno la valvola di irrigazione. Inoltre, il server è responsabile della gestione dei dati e della loro 
    organizzazione per garantire una facile interrogazione e visualizzazione.
4. Visualizzazione dei Dati
    Un aspetto fondamentale del progetto è la visualizzazione dei dati. Il server genera un grafico che rappresenta l'umidità del terreno e indica, 
    tramite segnali visivi, quando il sistema ha deciso di aprire la valvola per l'irrigazione. Questa visualizzazione consente una comprensione 
    immediata dello stato del sistema e delle decisioni prese in tempo reale.
5. Servizi Cloud
    Tutta l'architettura è basata su servizi cloud, che permettono di gestire e scalare il sistema in modo efficiente. I dati vengono inviati al cloud 
    per l'archiviazione e l’elaborazione, sfruttando la potenza di calcolo disponibile per eseguire l'analisi in tempo reale.

Workflow del Sistema:
- Il client legge i dati di umidità dal dataset e li invia al server tramite HTTP.
- Il server riceve i dati, li salva nel database e applica il modello di machine learning per predire se aprire la valvola di irrigazione.
- Il server visualizza un grafico interattivo con i dati di umidità del terreno e segnala quando la valvola è stata aperta.
- Il flusso di dati continua a essere aggiornato e monitorato, con decisioni di irrigazione prese in tempo reale sulla base delle previsioni del modello ML.

Obiettivi Didattici:
Questo progetto è stato progettato per esplorare e implementare vari concetti legati alla computazione pervasiva, ai servizi cloud, e al machine learning, 
offrendo un’applicazione pratica per la gestione intelligente delle risorse naturali. La combinazione di questi tecnologie consente di creare un sistema 
efficace e scalabile per ottimizzare l'uso dell'acqua in un sistema agricolo.

Tecnologie Utilizzate:
- Machine Learning per la previsione delle decisioni di irrigazione.
- HTTP per la comunicazione tra client e server.
- Database per l'archiviazione dei dati ricevuti.
- Servizi Cloud per la gestione scalabile dei dati e l'elaborazione in tempo reale.
- Grafico interattivo per la visualizzazione dei dati e delle decisioni.

Componenti del Repository:
- Codice per il client e il server.
- Codice per l’allenamento e l’applicazione del modello di machine learning.
- Codice per la visualizzazione dei dati tramite grafici.
- File di configurazione per la gestione dei servizi cloud.

Questo repository fornisce una soluzione completa per la gestione di un sistema di irrigazione basato su dati in tempo reale e tecnologie avanzate di 
analisi e previsione.