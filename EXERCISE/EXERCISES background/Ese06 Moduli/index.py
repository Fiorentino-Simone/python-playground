#try to import a module that is not installed
#import sys #sys is a module that contains functions for interacting with the operating system
#print(sys.builtin_module_names); #builtin_module_names is a list of the names of the built-in modules
#questi quindi sono tutti i moduli utilizzabili da sistema, senza la necessita di installarli, scritti in c
#altri moduli che sono sempre installati durante il processo di installazione però sono scritti in python, come os

import time; #time is a module that contains functions for manipulating time and date
#print(dir(time)); #dir is a function that returns a list of the names of the attributes of an object

import os; #os is a module that contains functions for interacting with the operating system
#la libreria os ci permette di utilizzare moltissimi metodi come path per controllare se è presente o no

#DOCUMENTAZIONE:
#https://docs.python.org/3/library/os.html #os.path
#https://docs.python.org/3/library/time.html #time.time

while True:
    if(os.path.exists("fruits.txt")):
        with open("fruits.txt", "r") as f:
            print(f.read());
    else:
        print("File not found");
    time.sleep(10);