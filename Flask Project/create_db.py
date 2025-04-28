import sqlite3

conn = sqlite3.connect('Flask Project/covid.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS covid 
              (aadhar_num INT NOT NULL, 
               name VARCHAR(255) NOT NULL, 
               age INT NOT NULL, 
               doses INT);''')
print ("Table created successfully")
conn.close()