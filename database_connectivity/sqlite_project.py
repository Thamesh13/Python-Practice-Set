import sqlite3

conn = sqlite3.connect('DB/covid.db')

cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS Covid_Data")

cursor.execute('''CREATE TABLE IF NOT EXISTS Covid_Data 
               (AADHAR_NUM INT PRIMARY KEY NOT NULL, 
               NAME VARCHAR(255) NOT NULL, 
               AGE INT NOT NULL, DOSES INT);''') 


while True:
    aadhar_num = input("Enter 5-digit valid Aadhar Number: ")
    if len(aadhar_num)==5:
        pass
    else:
        print("Aadhar number must contain 5 numbers exactly...")
        continue
        
    name = input("Enter your name as per your Aadhaar Card: ")
    
    age = int(input("Enter your age: "))
    
    dose = int(input("Vaccination dose(s) taken (0 or 1 or 2): "))
    if dose in [0,1,2]:
        break
    else:
        print("Enter a valid dosage number...")
        continue
    
cursor.execute('''INSERT INTO Covid_Data (Aadhar_num, name, age, doses) VALUES ( ?, ?, ?, ?)''', (aadhar_num, name, age, dose))

data=cursor.execute('''SELECT * FROM Covid_Data''')
for row in data:
    print(row)

conn.commit()

conn.close()
    