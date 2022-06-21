#pandas serve per creare un dataframe da una tabella 
#e lavorare con grandi quantità di dati, come ad esempio dati contenuti in un excel/json
#e permette di utilizzare le funzioni di analisi statistiche

import pandas;
#documentation of pandas:
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
#https://pandas.pydata.org/docs/

#and also andiamo ad utilizzare IPython che serve per creare una shell per lavorare con il dataframe
#visualizzare i dati in una maniera molto più facile e comprensibile

import IPython; #per usarla scrivere sulla power shell: ipython
df1 = pandas.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}); #creo un dataframe con 3 colonne e formato JSON
print(df1);
#ricordo che se voglio controllare tutti i metodi di un dataframe devo scrivere: dir(df1)

#per stampare la media ad esempio: 
print(df1.mean()); #questo è un esempio di analisi statistica 

#per stampare la media di una colonna:
print(df1["A"].mean());
