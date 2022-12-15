from customtkinter import *
from db import DbConnection
from user import User
from login import Login


class App(CTk):
    def __init__(self):
        super().__init__()
        self.db = DbConnection()
        self.currentUser: User = self.db.getLoggedInUser()
        if self.currentUser.userName is None:
            self.showLoginScreen()

    def showLoginScreen(self):
        Login(self, self.db)


if __name__ == "__main__":
    app = App()
    app.mainloop()
