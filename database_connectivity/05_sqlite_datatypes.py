# NULL -> None
# INTEGER -> int
# REAL -> float
# TEXT/CHAR/VARCHAR -> str
# BLOB -> bytes

import sqlite3  

# create connection to database
cnt = sqlite3.connect('DB/dt.db')  

cnt.execute('DROP TABLE IF EXISTS exam_hall;')

# Create a exam_hall relation
cnt.execute('''CREATE TABLE exam_hall(
NAME TEXT,
PIN INTEGER,
OCCUPANCY REAL,
LOGO BLOB);''')

# Open the logo file in read, binary mode
# read the image as binary data into a variable
fileh = open('image.jpg', 'rb')
img = fileh.read()

# Insert tuples for the relation
cnt.execute('''INSERT INTO exam_hall VALUES(
'centre-a',1125,98.6,?)''', (img,))
cnt.execute('''INSERT INTO exam_hall VALUES(
NULL,1158,80.5,?)''', (img,))

# Query the data, print the data and its type
# note: Printing the image binary data is impractical due to its huge size
# instead number of bytes are being printed using len()
cursor = cnt.execute('''SELECT * FROM exam_hall;''')
#cursor = [(1st record),(2nd record)]
for i in cursor:
    print(str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(len(i[3])))
    print(str(type(i[0]))+" "+str(type(i[1]))+" " +
          str(type(i[2]))+" "+str(type(i[3]))+"\n")