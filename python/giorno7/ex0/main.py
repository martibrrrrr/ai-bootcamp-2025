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
    data = list(reader)  # converto il testo in una lista

reorder_data = (sorted(data,key=surname))
print("Reorder Data:")
for index, line in enumerate(reorder_data, start = 1):
    print([index] + line)
with open("data2.csv", mode = "w", newline='') as fd:
    writer=csv.writer(fd)
    writer.writerow(header) #aggiungo l'intestazione
    writer.writerows(reorder_data)