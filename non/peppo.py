import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create the table
cursor.execute("CREATE TABLE your_table (id INT AUTO_INCREMENT PRIMARY KEY)")

# Display the table
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()
for row in result:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()