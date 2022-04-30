#FUNCTION: per le funzioni bisogna inzializzarle con def
from tkinter import Y; #per creare una costante


x = "prova variabile globale"; #variabile globale

def functionProva():
    x = "prova shadowing";
    print("Python is: " + x);
    global y;
    y = "Prova variabile globale inside"; #trasforma con la parola global una variabile visibile solo dentro una funzione NON privata ma GLOBALE

functionProva();

print("Python is: ",y);