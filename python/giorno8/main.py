import csv
import sqlite3

#creo SQLite file
conn = sqlite3.connect("my_database.db") #connettore
cur = conn.cursor() #cursore

cur.execute('''
        CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        year_of_birth INTEGER,
        gender TEXT,
        email TEXT,
        assignments INTEGER DEFAULT 0)
''')

conn.commit() #salvo il connettore

#Pulisce la tabella prima di inserire i nuovi dati
#cur.execute("DELETE FROM student")
#conn.commit()

with open("students.csv", "r") as fd:
    reader = csv.reader(fd, delimiter=";")
    next(reader) #salto l'intestazione
    saved_data = []
    for line in reader:
        line = [x.strip() for x in line]
        print(line)
        saved_data.append(line)

cur.executemany("INSERT INTO student (id,first_name,last_name,year_of_birth,gender,email,assignments) VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT DO NOTHING", saved_data)
conn.commit()

#studenti nati nel 2000
print("Student borned in 2000:")
cur.execute("SELECT first_name, last_name FROM student WHERE year_of_birth = 2000")
for line in cur.fetchall():
    print(line)

#la persona che ha consegnato più assignments
print("The best student, with the maximum number of assignment")
cur.execute("SELECT first_name,last_name,assignments FROM student WHERE assignments = (SELECT MAX (assignments) FROM student)")
for line in cur.fetchall():
    print(line)

#il cognome delle studentesse di nome JANE
print("The surname of all the Jane - student girl")
cur.execute("SELECT last_name FROM student WHERE first_name = 'Jane' AND gender = 'F'")
for line in cur.fetchall():
    print(line)

#stamapre la graduatoria degli studenti in base al numero di assignment consegnati
print("The student classification based on assignments")
cur.execute("SELECT first_name, last_name, assignments FROM student ORDER BY assignments DESC")
for line in cur.fetchall():
    print(line)

#BONUS
