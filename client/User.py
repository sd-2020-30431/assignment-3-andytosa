class User:
    def __init__(self, uid, username, password, email):
        self.uid = uid
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f'User {self.username} ({self.password})'

    def getID(self):
        return self.uid
