
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

#step 1
import sqlite3
import os


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")
    cursor = connection.cursor()
    connection.commit()

def insert_data(connection):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO example (id, name, age) VALUES (1, 'alice', 20)")
    cursor.execute("INSERT INTO example VALUES (2, 'bob', 30)")
    cursor.execute("INSERT INTO example VALUES (3, 'eve', 40)")
    cursor = connection.cursor()
    connection.commit()

def select_data(connection):
    cursor = connection.cursor()
    # SELECT CustomerName, City FROM Customers;
    cursor.execute("SELECT name, age FROM example")

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
