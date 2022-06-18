myFile = open("fruits.txt", "r"); #si setta che voglio leggere il file
print(myFile.read()); #stampa il contenuto del file si può fare solo una volta, da quando si apre il file
myFile.close(); #chiude il file

#per leggere il file con il blocco with e non devo chiudere il file
with open("fruits.txt", "r") as myFile:
    print(myFile.read());

#per scrivere un file
with open("vegetables.txt", "w") as myFile:
    myFile.write("Banana\n");
    myFile.write("Apple\n");
    myFile.write("Orange\n");
    myFile.write("Cherry\n");
    myFile.write("Pineapple\n");
    myFile.write("Strawberry\n");

#per aggiungere del testo al file
with open("vegetables.txt", "a") as myFile:
    myFile.write("Potato\n");
    myFile.write("Tomato\n");
    myFile.write("Carrot\n");

#per scrivere e leggere il file con il blocco with assieme
with open("fruits.txt", "r+") as myFile:
    print(myFile.read());
    myFile.write("\nCucumber");
    myFile.seek(0); #torna all'inizio del file con il cursore
    print(myFile.read());