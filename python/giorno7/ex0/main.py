import csv

def surname(riga):
    # funzione f per restituire il secondo elemento della tupla (cognome).
    return riga[1]

with open("data.csv") as fd: #associo il file importato alla variabile fd
    reader = csv.reader(fd) #creo oggetto reader che itera sulle righe del file .csv
    for line in reader:
        print(line)
    #con "with open" chiudo file automaticamente una volta terminata la lettura

with open("data.csv", mode="r", newline='') as fd:
    reader = csv.reader(fd)
    header = next(reader) #per leggere l'intestazione così la rimovo dal testo che leggo successivamente
    #surname_index = header.index("Surname")  #oppure
    data = list(reader)  # converto il testo in una lista

reorder_data = (sorted(data,key=surname))
print("Reorder Data:")
for index, line in enumerate(reorder_data, start = 1):
    print([index] + line)
with open("data2.csv", mode = "w", newline='') as fd:
    writer=csv.writer(fd)
    writer.writerow(header) #aggiungo l'intestazione
    writer.writerows(reorder_data)

#BONUS name + surname
#import csv

#riordino prima in base al cognome e poi in base al nome
def surname_name(riga):
    # funzione f per restituire il secondo elemento della tupla (cognome).
    return (riga[1],riga[0])

with open("data2_bonus.csv", mode="r", newline='') as fd: #associo il file importato alla variabile fd
    reader = csv.reader(fd) #creo oggetto reader che itera sulle righe del file .csv
    header = next(reader) #per leggere l'intestazione così la rimovo dal testo che leggo successivamente
    data = list(reader)  # converto il testo in una lista
index_name=header.index("Name")
index_surname=header.index("Surname")
def f(x):
    return(x[index_surname],x[index_name])
reorder_data = sorted(data,key=f)
#reorder_data = sorted(data,key=surname_name)
print("Reorder Data:")
for index, line in enumerate(reorder_data, start = 1):
    print([index] + line)

with open("reorder_data2_bonus.csv", mode = "w", newline='') as fd:
    writer=csv.writer(fd)
    writer.writerow(header) #aggiungo l'intestazione
    writer.writerows(reorder_data)

#SPIEGAZIONE

#1. lambda
"""è un altro modo di definire una funzione. 
scrivo la funzione in modo più breve
le lambda vanno scritte tutte sulla stessa riga
non si può usare yield (generatore) lambda x:yield x NO!! devo scrivere una espressione dopo
def f(x):
    return x**2
assert f(2)==4

f2 = lambda x: x**2 #non devo inserire il return usando la funzione lambda
assert f(2)==4

f3 = lambda x: (x, x**2) #tupla
assert f3(2) == (2,4)

lambda x:x #return x -> x
(lambda x:x**2)(2) # =4 la funzione è sparita perchè non ho associato un nome
import this #linee guida del buon programmatore
"""
#2. enumerate
"""Range: 
 list(range(1,10))
 for name in ["Paola","Giulia","Enza"]:
    print(name)
 se voglio aggiungere il numero ed incrementarlo in base alla sequenza che sto printando
 posso usare ENUMERATE. ritorna una sequenza di tuple
 
 for idx, name in enumerate(["Paola","Giulia","Enza"],1): #parto dall'indice numero 1
    print(idx,name)    

#è uguale a fare
idx=0
for name in ["Paola","Giulia","Enza"]:
    print(idx,name)
    idx +=1
    
list(enumerate([]) #resituisce tuple con due elementi dentro
[(1,'Paola'),(2,'Giulia'),(3,'Enza')]
 """