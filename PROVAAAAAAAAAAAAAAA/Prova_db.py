import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Prova_db")




