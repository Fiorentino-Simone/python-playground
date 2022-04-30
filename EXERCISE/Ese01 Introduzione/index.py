x="Ciao"; #le variabili non utilizzano let o una tipologia 
y=12;
#si accede ai metodi tramite la dot notation e bisogna fare il cast con il metodo str da int a stringa
# oppure possiamo fare quello con la virgola che permette tutto es: print("Ciao",x,y);
print("STAMPA VARIABILI: ",x,y);

##VARIABILI: 
#si possono specificare la tipologia 
prova = str(3);    # prova will be '3'
prova2 = int(3);    # prova2 will be 3
prova3 = float(3);  # prova3 will be 3.0

print(type(x)); #serve per capire il tipo

#Concetto di unpacking: python permette di creare una collezione e successivamente andare ad assegnare a quelle variabili
# rispettivamente il valore indicato
fruits = ["apple", "banana", "cherry"];
x, y, z = fruits;

print(x);
print(y);
print(z);