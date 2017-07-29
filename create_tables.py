import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" # id int; id INTEGER PRIMARY KEY - it will assign automathically number, we will need to assign only username and password
cursor.execute(create_table)



connection.commit()
connection.close()
