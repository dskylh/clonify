class User:
    def __init__(self, userName, password, loggedIn=False):
        self.userName = userName
        self.password = password
        self.loggedIn = loggedIn


    def checkPassword(self, password: str) -> bool:
        return password == self.password

