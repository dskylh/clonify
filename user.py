class User:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def checkPassword(self, password: str) -> bool:
        return password == self.password

