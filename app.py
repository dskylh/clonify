from customtkinter import *

import login
from db import DbConnection
from login import Login
from player import Player


class App(CTk):
    def __init__(self):
        super().__init__()
        self.db = DbConnection()
        self.library = self.db.getMusics("")
        self.player = Player(library=self.library)
        self.showLoginScreen()
        self.songButton = CTkButton(self, text="Song", command=self.player.playMusic)
        self.songButton.pack()

    def showLoginScreen(self):
        Login(self, self.db)


if __name__ == "__main__":
    app = App()
    app.mainloop()
