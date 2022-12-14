from customtkinter import *
from db import DbConnection
from login import Login


class App(CTk):
    def __init__(self):
        super().__init__()
        self.db = DbConnection()
        self.showLoginScreen()

    def showLoginScreen(self):
        Login(self, self.db)


if __name__ == "__main__":
    app = App()
    app.mainloop()
