import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id # "_id" because "id" is python keyword and can not be used as variable name
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row is not NONE:   # = if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user
        
