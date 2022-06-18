def mean(*args): 
    # mean of a list of numbers, ma i parametri sono una lista di numeri infiniti
    #args è una tupla
    return sum(args) / len(args);

print(mean(1, 2, 3, 4, 5));

#parole tutte in maiuscolo e ordinate alfabeticamente
def ordinaParole(*args):
    args = [x.upper() for x in args]
    return sorted(args);

#i parametri sono una lista di parole, anch'essa può essere di lunghezza infinita
print(ordinaParole("ciao", "miao", "pluto", "pippo"));

#se vogliamo avere una funzione con dei keyword arguments
def funzione(**kwargs):
    return kwargs;
#bisogna passare due asterischi e poi andare a nominare questi parametri
print(funzione(a=1, b=2, c=3));