import csv
import random
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


"""
#BONUS----------------------BONUS----------------BONUS------------------------------
from datetime import datetime, timedelta
students_without_assignments = []
assignment_data = []

conn2 = sqlite3.connect("my_database2.db") #connettore
cur2 = conn2.cursor() #cursore

#creo la tabella
cur2.execute('''
            CREATE TABLE IF NOT EXISTS assignments(
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            delivery_date TEXT)
''')
conn2.commit()
#assegno i compiti come nel file databade1

students_assignments = {
    1: 5,  # Studente 1 ha 5 compiti
    2: 3,  # Studente 2 ha 3 compiti
    3: 6,  # Studente 3 ha 6 compiti
    4: 4,  # Studente 4 ha 4 compiti
    8: 5,  # Studente 8 ha 5 compiti
    9: 4,  # Studente 9 ha 4 compiti
    10: 4,  # Studente 10 ha 4 compiti
    11: 5,  # Studente 11 ha 5 compiti
    12: 5  # Studente 12 ha 5 compiti
}
start_date = datetime(2025, 1, 1)
expanded_data=[]
output_file=[]

for student_id, num_assignments in students_assignments.items():
    for i in range(num_assignments):
        new_date= start_date + timedelta(days=random.randint(-2,2))
        expanded_data.append((student_id,new_date.strftime("%Y-%m-%d"))) #prende un solo argomento quindi passo una tupla


cur2.executemany("INSERT INTO assignments (student_id, delivery_date) VALUES (?, ?)", expanded_data) #lascio genereare nuovo id da solo
conn2.commit()
#scrivo students_without_assignments.csv
with open("students_without_assignments.csv","w",newline="", fd):
writer = csv.writer(fd,delimiter=";")
    writer.writerow(new_header)
    writer.writerow(students_without_assignments)

#scrivo soglio gli assignments.csv
with open("assignments.csv","w",newline="") as fd:
    writer = csv.writer(fd, delimiter=";")
    writer.writerow(["id","student_id","delivery_date"]) #intestazione
    for line, (student_id, delivery_date) in enumerate(expanded_data, start=1 ):
        writer.writerow([line,student_id, delivery_date])

cur2.execute('''
    SELECT student.first_name, student.last_name, assignments.delivery_date
    FROM student
    JOIN assignments ON student.id = assignments.student_id
    ORDER BY assignments.delivery_date ASC
''')
for line in cur2.fetchall():
    print(line)
"""
