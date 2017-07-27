class User:
    def __init__(self, _id, username, password):
        self.id = _id # "_id" because "id" is python keyword and can not be used as variable name
        self.username = username
        self.password = password
