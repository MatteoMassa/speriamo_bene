#step 1
import sqlite3



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


connection = sqlite3.connect("test.db")
# create_table(connection)
# insert_data(connection)

select_data(connection)

# MENU
# 1. inserisci nuova riga nella tabell
# 2. stampa tutta la tabella
# 3. stampa una riga della tabella in base all'ID