# import sqlite3

# # Connecting to sqlite
# # connection object
# connection_obj = sqlite3.connect('DB/per.db')

# # cursor object
# cursor_obj = connection_obj.cursor()

# connection_obj.execute("DROP TABLE IF EXISTS PER")

# connection_obj.execute("""CREATE TABLE PER(
#   Email varchar(255),
#   Name varchar(50),
#   Score int
#   );""")

# connection_obj.execute(
#     """INSERT INTO PER (Email,Name,Score) VALUES ("perk1@gmail.com","per1",25)""")
# connection_obj.execute(
#     """INSERT INTO PER (Email,Name,Score) VALUES ("perk2@gmail.com","per2",15)""")
# connection_obj.execute(
#     """INSERT INTO PER (Email,Name,Score) VALUES ("perk3@gmail.com","per3",36)""")
# connection_obj.execute(
#     """INSERT INTO PER (Email,Name,Score) VALUES ("perk4@gmail.com","per4",27)""")
# connection_obj.execute(
#     """INSERT INTO PER (Email,Name,Score) VALUES ("perk5@gmail.com","per5",40)""")
# connection_obj.execute(
#     """INSERT INTO PER (Email,Name,Score) VALUES ("perk6@gmail.com","per6",36)""")
# connection_obj.execute(
#     """INSERT INTO PER (Email,Name,Score) VALUES ("perk7@gmail.com","per7",27)""")

# # CURSOR METHOD:
# # data=connection_obj.execute('''select*from PER''')
# # print(data)

# # for row in data:
# #     print(row) 

# # FETCHALL METHOD:
# cursor=connection_obj.execute('''select*from PER''')
# data=cursor.fetchall()
# print(data)

# for row in data:
#     print(row) 


# connection_obj.commit()

# # Close the connection
# connection_obj.close()


# -----------------------------------------------------------------------------

# # Read All Rows:
# import sqlite3

# # Connecting to sqlite
# # connection object
# connection_obj = sqlite3.connect('DB/per.db')

# # cursor object
# cursor_obj = connection_obj.cursor()

# # to select all column we will use
# statement = '''SELECT * FROM PER'''

# cursor_obj.execute(statement)

# print("All the data")
# output = cursor_obj.fetchall()
# print(output)

# for row in output:
#   print(row)

# connection_obj.commit()

# # Close the connection
# connection_obj.close()

# --------------------------------------------------------------------------------------
# # Read Some Rows:

# import sqlite3

# # Connecting to sqlite
# # connection object
# connection_obj = sqlite3.connect('DB/per.db')

# # cursor object
# cursor_obj = connection_obj.cursor()

# # to select all column we will use
# statement = '''SELECT * FROM PER'''

# cursor_obj.execute(statement)

# print("Only 3 No's of data")
# output = cursor_obj.fetchmany(3)
# print(output)
# for row in output:
#   print(row)

# connection_obj.commit()

# # Close the connection
# connection_obj.close()

# --------------------------------------------------------------------------------------------

# # Read Only one Row:

# import sqlite3

# # Connecting to sqlite
# # connection object
# connection_obj = sqlite3.connect('DB/per.db')

# # cursor object
# cursor_obj = connection_obj.cursor()

# # to select all column we will use
# statement = '''SELECT * FROM PER'''

# cursor_obj.execute(statement)

# print("Only one data")
# output = cursor_obj.fetchone()
# print(output)

# connection_obj.commit()

# # Close the connection
# connection_obj.close()


# -------------------------------------------------------------------------------------

# # WHERE Clause
# import sqlite3

# connection = sqlite3.connect('DB/per.db')
# cursor = connection.cursor()

# # WHERE CLAUSE TO RETRIEVE DATA
# cursor.execute("SELECT * FROM PER WHERE Score > 30")

# print(cursor.fetchall())

# connection.commit()
# connection.close() 


# ----------------------------------------------------------------------------------

# import sqlite3

# connection = sqlite3.connect('DB/per.db')
# cursor = connection.cursor()

# # WHERE CLAUSE TO RETRIEVE DATA
# cursor.execute("SELECT Name,Score FROM PER WHERE Score < 30")

# print(cursor.fetchall())

# connection.commit()
# connection.close() 