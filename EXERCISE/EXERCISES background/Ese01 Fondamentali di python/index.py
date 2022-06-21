spent = 0;
donated = 4;

total_price = spent + donated;

print("Total price:", total_price);

#Array/list
array = [9, "Hello", [87, "World"]];
print(array);

#Array/list con il range --> funzione che restituisce tutti i numeri in quel range
array = list(range(1, 10)); #bisogna fare il cast in lista
#il terzo parametro è lo step di valori che salta numeri 
print(array);

print(dir(array)); #restituisce tutti i metodi della list
print(dir(__builtins__)); #restituisce tutti i metodi della libreria

mysum = sum(array);
length = len(array);
print("Average:", mysum/length); #or max per calcolare il massimo

student_grades = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
number = student_grades.count(10.0) #restituisce il numero di volte che compare un valore in una lista
username = "Ciao";
print(username.upper()); #converte tutto in maiuscolo
print(username.lower()); #converte tutto in minuscolo
print(username.capitalize()); #converte la prima lettera in maiuscolo
print(username.title()); #converte tutte le prime lettere in maiuscolo
print(username.swapcase()); #inverte tutte le maiuscole e le minuscole
print(username.replace("Ciao", "Ciao")); #rimpiazza una stringa con un'altra
print(username.find("Ciao")); #restituisce la posizione della stringa
print(username.isalpha()); #restituisce True se la stringa contiene solo lettere
print(username.isalnum()); #restituisce True se la stringa contiene solo lettere e numeri
print(username.isnumeric()); #restituisce True se la stringa contiene solo numeri
print(username.isupper()); #restituisce True se la stringa contiene solo lettere maiuscole
print(username.islower()); #restituisce True se la stringa contiene solo lettere minuscole


#Dictionary or Json
#Dictionary --> una lista di coppie chiave-valore
#Json --> una stringa che contiene una lista di coppie chiave-valore
student_grades = {"marry" : 8.775, "james" : 9.1, "carl" : 9.3, "david" : 8.1, "julie" : 9.4};
print(student_grades);
print(student_grades["marry"]);
print(student_grades.values()); #restituisce tutti i valori del dict
print(student_grades.keys()); #restituisce tutte le chiavi del dict
print(student_grades.items()); #restituisce tutte le coppie chiave-valore del dict --> come stampare il dict

#tuples
#tuples --> una lista che non può essere modificata
example_tuple = (1, 2, 3, 4, 5);
print(example_tuple); #non si possono usare metodi come append, insert, remove, pop, etc perchè POSSIBILI SOLO NELLA lista
print(example_tuple[0]); #restituisce il valore in posizione 0 come per la lista

#Array methos
#append --> aggiunge un elemento alla fine della lista
#insert --> aggiunge un elemento in una posizione specifica
#remove --> rimuove un elemento dalla lista
#clear --> cancella tutti gli elementi della lista
#pop --> rimuove un elemento dalla lista
#sort --> ordina la lista
#reverse --> inverte la lista
#count --> restituisce il numero di volte che compare un valore in una lista
#index --> restituisce la posizione dell'elemento in una lista
#copy --> restituisce una copia della lista

example_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; #stessa cosa funziona con le liste di caratteri
print(example_slice[0:5]); #restituisce una lista con i primi 5 elementi
print(example_slice[5:]); #restituisce una lista con i restanti elementi
print(example_slice[:5]); #restituisce una lista con i primi 5 elementi

#index negativo, sarebbe come se fosse una lista da destra verso sinistra
print(example_slice[-1]); #restituisce l'ultimo elemento della lista


#definisco la funzione per calcolare la media
def mean(values):
    if(type(values) == dict):
        return sum(values.values())/len(values);
    else:
        return sum(values)/len(values);

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print(mean(numbers));
print(mean(student_grades)); 


#abs(x) #restituisce il valore assoluto di x

example_user_input = float(input("Insert a number: "));
print(example_user_input);
message = "Hello World " + str(example_user_input);
print(message);

for i in range(1, 10):
    print(i); #stampa i numeri da 1 a 9

# il for nei dictonary
for key, value in student_grades.items():
    print(key, value);

#example of while
i = 0;
while i < 10:
    print(i);
    i += 1;

#while with input name
name = "";
while name == "":
    name = input("Insert your name: ");
print("Hello", name);

#use of break and continue in a while
i = 0;
while True:
    i += 1;
    if i == 10:
        break;
    if i % 2 == 0:
        continue;
    print(i);

#use of try catch 
try:
    print(1/0);
except ZeroDivisionError:
    print("You can't divide by zero");