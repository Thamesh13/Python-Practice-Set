import sqlite3

# Connecting to sqlite connection object
conn = sqlite3.connect('DB/sample.db')
print('db created successfully')

conn.close()
print('db closed successfully')