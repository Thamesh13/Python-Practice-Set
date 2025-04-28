# There are two ways of using the INSERT INTO statement for inserting rows:
# Only values: INSERT INTO table_name VALUES (value1, value2, value3,…);
# Column names and values both: INSERT INTO table_name (column1, column2, column3,..) VALUES ( value1, value2, value3,..);

# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('DB/student.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Creating table
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255),
SECTION VARCHAR(255));"""
cursor.execute(table)

# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')''')

print('Enter one user values:')
s_name = input('Enter Student Name:')
s_class = input('Enter Student Class:')
s_section = input('Enter Student Section:')

cursor.execute(f'''INSERT INTO STUDENT VALUES ("{s_name}", "{s_class}", "{s_section}")''')

# Display data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM STUDENT''')
print(data)
for row in data:
    print(row)

# Commit your changes in the database    
conn.commit()

# Closing the connection
conn.close()
