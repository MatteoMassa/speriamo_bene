#step 1
import sqlite3
import os


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS persone (id INTEGER, name TEXT, age DATE, PRIMARY KEY(id)")
    cursor.execute("CREATE TABLE IF NOT EXISTS economic (id INTEGER, salary TIMESTAMP, Job TEXT, FOREIGN KEY(id) REFERENCES persone(id)")
    cursor = connection.cursor()
    connection.commit()


id, salary, job, id

def insert_data(connection):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO persone (id, name, age) VALUES (1, 'alice', '2001-03-25')")
    cursor.execute("INSERT INTO persone VALUES (2, 'bob', '2013-11-01')")
    cursor.execute("INSERT INTO persone VALUES (3, 'eve', '1978-07-12')")

    cursor.execute("INSERT INTO economic (id, name, age) VALUES (id, 1200, 'Giardiniere')")

    cursor = connection.cursor()
    connection.commit()

def select_data(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT name, age FROM persone")
    
    #cursor.execute("SELECT * FROM economic")

    rows = cursor.fetchall()
    print(type(rows))
    print("Data read from database")
    for row in rows:
        print(row)


# check if test.db exists
if not os.path.exists("test.db"):
    print("creating test.db")
    connection = sqlite3.connect("test.db")
    create_table(connection)
    insert_data(connection)
else:
    print("test.db already exists")
    connection = sqlite3.connect("test.db")

select_data(connection)

# MENU CLI command line interface
# 1. inserisci nuova riga nella tabell
# 2. stampa tutta la tabella
# 3. stampa una riga della tabella in base all'ID

# 1. inserisci nuova riga nella tabella
# python database.py --insert 4 gianni 34

# 2. stampa tutta la tabella
# python database.py --print

# 3. stampa una riga della tabella in base all'ID
# python database.py --print-line 2


# MENU CLI: argparse


# SITO FLASK





CREATE TABLE IF NOT EXISTS persone 
(
    id INTEGER, 
    name TEXT, 
    age DATE, 
)


CREATE TABLE IF NOT EXISTS economic
(
    id INTEGER, 
    salary TIMESTAMP, 
    Job TEXT, 
    persona_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (persona_id) REFERENCES persone(id)
);
