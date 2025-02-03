import os

#Programmazione a ogetti: classi e istanze
class Studente:
    ore_settimanali = 36 #variabili di istanza
    corpo_studentesco= 0 #variabili di classe
    def __init__(self,nome,cognome,corso): #metodo costruttore init = inizializzazione
    #attributi:nome cognome corso
    #istanza = ciascun oggetto creato dalla classe,
    #l'stanza rappresenta l'oggetto a cui associo le proprietà passate nel metodo inizializzazione
    #self rappresenta una referenza a ciascun oggetto creato dalla classe.
    #self: istanza passata automaticamente da python
    #init inizializza le proprietà di ciascu oggetto o istanza
        self.nome = nome
        self.cognome=cognome
        self.corso=corso
        Studente.corpo_studentesco+=1
    #variabili dell'istanza =  attributi della classe

    # aggiungo un secondo metodo alla classe
    def scheda_personale(self):
        return f"Scheda Studente:\n " \
               f"Nome:{self.nome}\n" \
               f"Cognome:{self.cognome}\n "\
               f"Corso di Studi:{self.corso}\n"\
               f"Ore Settimanali:{self.ore_settimanali}"

#creo degli studenti partendo dalla stessa classe: DUE ISTANZE
studente_uno = Studente("Py","Mike","programmazione")
studente_due = Studente("Marta","Bruno","matematica")
print(studente_due)
print(studente_uno)

print(studente_uno.scheda_personale()) #secondo metodo
print(Studente.scheda_personale(studente_uno)) #come parametro passo l'istanza

#incremento allo studente 1 le ore settimanali
studente_uno.ore_settimanali+=4
print(studente_uno.scheda_personale())

#stampo e caratteristiche di
print(Studente.__dict__)
print(studente_uno.__dict__)







"""class Directory:
    def __init__(self):
        self.contacts = []
        self.name_index ={}
        self.surname_index = {}
        self.phone_index = {}

    def __len__(self):
        return len(self.contacts)

    def add(self, contact):
        self.contacts.append(contact)

        if contact.name not in self.name_index:
            self.name_index[contact.name] = []
        self.name_index[contact.name].append(contact)

        if isinstance(contact, Person) and contact.surname:
            if contact.surname not in self.surname_index:
                self.surname_index[contact.surname]=[]
                self.surname_index[contact.surname].append(contact)

        if contact.phone:
            if contact.phone not in self.phone_index:
                self.phone_index[contact.phone] = []
                self.phone_index[contact.phone].append(contact)
        def query(self, name):
            self.name_index.get(name,[])

        def find(self,search_contact):
            result = []
            if search_contact in self.phone_index:
                result =self.phone_index[search_contact]
            else:
                result+=self.query(search_contact)
                result+=self.surname_index.get(search_contact, [])
            return result

class Person:
    def __init__(self,name,surname,phone=""):
        self.name = name
        self.surname = surname
        self.phone = phone

class Business:
    def __init__(self,name,phone=""):
        self.name=name
        self.phone=phone

directory = Directory()

directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))

print([el.name for el in directory.find("Hamilton")])  # Ricerca per cognome
#print([el.name for el in directory.find("01-234-567")])  # Ricerca per numero
#print([el.name for el in directory.find("Vedrai")])

"""

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __iter__(self):
        return iter([self.name, self.surname])


rigel = Person("Rigel", "Di Scala")
list(rigel)
['Rigel', 'Di Scala']
" ".join(rigel)
'Rigel Di Scala'
#if name.lower()=="rigel":
#    print(name)

nome = "rigel di scala"
"rigel di scala".capitalize()
#converto la stringa in una sequenza di sottostringhe:
#split in base allo spazio
#per ogni parola
def convert(s):
    words = s.split()
    words = [words.capitalize() for word in words]
    return " ".join(words)
convert(nome)
nome.startswith("Rigel")

#FILE
import os
print(os.listdir())
name="pippo.txt"
fd2 = open(name,"w")
fd2.write("Ciao!")
fd2.close() #i file vanno sempre chiusi. sia in lettura che in scrittura. libero spazio
fd2=open(name,"r")
print(fd2.read())

with open(name,"r") as fd3:
    print(fd3.read())
#eccezione: uscendo dal blocco chiude automaticamente il file

text = input("Comando? ") # INPUT blocca il programma e lo faccio diventare interattivo
print(text)

#esempio salvataggio nome dato dall'utente
text = ""
while text == "":
    text = input(" Per favore, inserire il nome:")
print(f"il tuo nome e' {text}")

#oppure:
while True: # text == ""
    text = input(" Per favore, inserire il nome corretto:")
    if text:
        break
print(f"il tuo nome e' {text}")

#chiedere di inserire un file: aggiungere il percorso file
text = ""
while text == "":
    text = input(" Per favore, inserire il percorso del file:")
print(f"il tuo file e' {text}")

#operatore tricheco
text = ""
#while text == "":
#posso sostituirlo da... è equivalente a...
#while not (text := ""):

def calculator():
    while True:
        user_input = input("inserisci operazione")
        if user_input.lower()=="quit":
            print("Arrivederci!")
            break
        #try:
        #    parts = users_input.split()

#LEZIONE 03.02.2025
help(sorted)
#sorted(iretable,/,*,key=None, reverse=False)
#riordina una frequenza ordinata. non riordina la variabile stessa
#ritonrna le lettere in ordine ascendente(ogni lettera è associata ad
# un numero che cresce, e posso quindi ordinarlo in ordine ascendente o discendente)

#lista di tuple.ogni tupla contiene due elementi
students = [("Marta","Zeta"),("Rosa","Alfa"),("Alba","Gamma")]
list(sorted(students))
def f(student):
    # funzione f per restituire il secondo elemento della tupla (cognome).
    return student[1]
# ordino con sorted il cognome
list(sorted(students, key=f))

#differenza tra dichiarazione ed espressione:
#import: keyword che crea una dichiarazione
#la dichiarazione importa un modulo
#I MODULI importano o creano un nome all'interno del main space attuale
#un modulo è un contenitore per classi e funzioni. Li organizza e rende importabili in altre parti del codice

#dobbiamo creare un file
#file1.py
PI=3.14
def foo():
    """Do somthing"""
#file2.py
#from file1 import PI, foo

#ALGORITMI DI RANDOMIZZAZIONE
#random
#contiene diverse funzioni con dati randomici
#uso generare sequenze di numeri random
#selezionare in maniera casuale elementi di una sequenza
#mischiare una sequenza

import random
random.randint(1,10)
li=[1,42] #sceglie tra i numeri scritti in li
random.choice(li)

range(1,3)

#random.randrange. scelgo un range
#random.random sceglie un  numero random tra 0 e 1 in float
0.1*random.randint(1,10) #per ottenere numero random tra 0 e 1, con precisione float 0.1
float("{}.{}".format(random.randint(1,10), random.randint(1, 99)))

random.seed #ALGORITMO CASUALE PARTENDO DA UN SEME. è deterministico come algoritmo
#se non ci fosse un seme(punto di partenza), avrei sempre la stessa frequenza
#esempio
import random
random.seed(3)
print(random.randint(1,10))

#criptografia
#per vedere la fonte di randomizzazione di dati
# sul terminale: cat /dev/rand

dir(random)
help(random.sample)
#prova
li = (1,2,3)
random.sample(li,2)
#prova
li = [1,2,3]
random.shuffle(li)

#jason(JavaScript Object Notation)
#è un modo per serializzare i dati
# JSON è usato per scambiare dati sul web
#serializziamo l'oggetto in una sua rappresentazione (stringa)
import json
a = {1: ["a","bbbb","c"]}
a
json.dumps(a) #restituisce una stringa
type(a) #dict
# dumps = scarica (dump) + stringa (s)
json.loads(s) #carico la stringa e ritorna il suo oggetto
#restituisce {'1': ['a','bbbb','c']}
#la chiave del dizionario "1" era un numero. in json diventa una stringa

json.loads(s)["1"]
#restituisce ['a','bbbb','c']

{int(k): v for k, v in json.loads(s).items()} #stringcomhompreation
s
a.items() #items = chiavi e valori
d = {1:"a", 2:"b"}
list(a.items())
list(d)
list(d.items())

d2={}
for k,v in d.items():
    d2[v] = k
d2 #ho invertito il dizionario
{int(k): v for k, v in json.loads(s).items()} #stringcomhompreation

d3 = {}
for k,v in json.loads(s).items():
    d3[int(k)] = v
d3 #per stampare


#IMPORT CSV
import csv

csv_test = "1,33,45,67"
csv_test.split(",")
#['1', '33', '45', '67']

csv_test = '"Martina","rigel"' #se ho delle virgole nelle stringhe sevo usare questa impostazione
csv_test.split(",")

csv_test = '"ciao, come stai?";"va bene, ok";" ok,ok;ok "'
csv_test.split(";") #separa bene. ma se usano un punto e virgola

#idea di prova
# csv_test.split('";')
# #così separa bene, ma devo poi pulire il testo. rimandono dei " nelle frasi

import csv
#with open("data.csv",'w',newline='')
with open("data.csv") as fd:
    reader = csv.reader(fd) #puntatore al file
    reader.writerow(['str']+['gkjk'])
    for line in reader:
        print(line) #stampo ciascuna riga di testo

#python3 -m venv .env
# -m = invoca un modulo
#venv invoca il modulo venv spazio virtuale
# .env è il nome del nuovo ambiene
#attivazione nuovo ambiente
#C:\> .env\ .......... vedi slides
#quando facciamo il commit non includiamo il .emv
#installazione di un pacchetto mediante pip
#su pypi.org trovo i progetti python pubblici
#pacchetto: openpyxl apro .py su excell

#CANCELLARE FILE
#pip install --upgrade pip
#pipi install -U
#which python3
#deactivate esco dall'ambiente virtuale

#learn Git Branching

#exercism esercizi per python

def factorial(n):
    if n > 1 :
        return n*factorial(n)
    else
        return 1
assert factorial(5) == 120

#le classi possono rimpiazzare le funzioni ricorsive
class Factorial:
    def __init__(self,start):
        self.state = start
        self.n = start
    def next(self):
        self.state *= start
        self.n -= 1
factorial_5 = Factorial(5)
result(factorial_5)
