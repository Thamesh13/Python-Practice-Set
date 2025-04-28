import sqlite3

# Connecting to sqlite connection object
connection_obj = sqlite3.connect('DB/data.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS DATA")

# Creating table
table = """ CREATE TABLE DATA (
            Email VARCHAR(255) NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Score INT
        ); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()