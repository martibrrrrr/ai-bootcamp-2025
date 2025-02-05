import sqlite3
import csv

#Parte 1
with open("data.csv", encoding='utf-8') as fd:
    reader = csv.reader(fd)
    saved_data = []
    for line in reader:
        print(line)
        saved_data.append(line)

data = saved_data[1:]


#Parte 2
conn = sqlite3.connect("my.db")
cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS agents (
        id INTEGER PRIMARY KEY,
        QuotaAmount INTEGER,
        Month INTEGER,
        Agent TEXT,  
        Username TEXT
    )''')
conn.commit()


cur.executemany(
    "INSERT INTO agents (QuotaAmount, Month, Agent, Username) VALUES (?, ?, ?, ?)",
    data
)
conn.commit()

cur.execute("SELECT DISTINCT Agent FROM agents")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT Agent, SUM(QuotaAmount) "
            "FROM agents "
            "GROUP BY Agent "
            "ORDER BY SUM(QuotaAmount) DESC")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT Month, SUM(QuotaAmount) "
            "FROM agents "
            "GROUP BY Month "
            "ORDER BY SUM(QuotaAmount) DESC")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT Month, Agent, MAX(QuotaAmount) "
            "FROM agents "
            "GROUP BY Month "
            )
row = cur.fetchall()
for row in rows:
    print(row)

cur.close()