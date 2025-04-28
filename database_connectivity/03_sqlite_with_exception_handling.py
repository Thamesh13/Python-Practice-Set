import sqlite3

try:
    
    # Connect to SQLite DB using conenct() method by passing name of DB 'sql.db'
    sqliteConnection = sqlite3.connect('DB/sql.db')
    # Create cursor() method on connection instance/object which will execute our query 
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Write a SQL query in string format and execute it by calling the execute() method on the cursor object
    query = 'select sqlite_version();'
    cursor.execute(query)

    # Fetched from the server by using the fetchall() method and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # Close the cursor
    cursor.close()

# Handle errors
except sqlite3.Error as error:
    print('Error occured - ', error)

# Close DB Connection irrespective of success or failure
finally:
    
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')