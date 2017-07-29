import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" # id int; id INTEGER PRIMARY KEY - it will assign automathically number, we will need to assign only username and password
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" # id int; id INTEGER PRIMARY KEY - it will assign automathically number, we will need to assign only username and password
cursor.execute(create_table)

# cursor.execute("INSERT INTO items VALUES('test', 10.99)")

connection.commit()
connection.close()
