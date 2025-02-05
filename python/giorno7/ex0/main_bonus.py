import csv
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