import sys;
import os;
import time; 
import pandas;  # installata all'interno dell'ambiente di python

#possiamo utilizzare il comando pip per installare un modulo che non è presente al momento dell'installazione del programma
#pip3.10 install <nome_modulo>
#in questo caso noi vogliamo installare il modulo pandas per lavorare con dei dati in csv
#pip3.10 install pandas --> COMANDO NEL TERMINALE NON QUELLO DI PYTHON
#se non funziona il comando prima usare: python -m pip install pandas 

while True:
    if(os.path.exists("temps_today.csv")):
        with open("temps_today.csv", "r") as file:
            data = pandas.read_csv(file); # leggo il file csv e lo memorizzo in una variabile
            print(data); # data è un dataframe di pandas --> è una tabella di dati in csv
            print(data.mean()); # stampo la media dei valori delle temperature
            print(data.mean()["st1"]); # stampo la media dei valori delle temperature della colonna st1
            #andiamo ad avere le min di ogni colonna (ricordo che le colonne nei csv sono divisi dalla virgola)
    else:
        print("File non trovato");
    time.sleep(10);


