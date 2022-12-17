import customtkinter
from SongSelect import SongSelect
from db import DbConnection
from login import Login
from player import Player
from music import Music
from typing import Optional


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.db = DbConnection()
        self.library = self.db.getMusics("")
        self.player = Player(library=self.library)
        self.loggedInUser = self.db.getLoggedInUser()
        self.currentMusic: Music
        print(self.loggedInUser.userName)
        self.login: Optional[Login] = None
        if self.loggedInUser.userName is None:
            self.login = Login(self, self.db)
            self.login.grab_set()
        print(self.login)
        self.musicNameList = [music.musicName for music in self.library]
        self.logoutButton = customtkinter.CTkButton(self, text="Log Out", command=self.logOutUser)

        self.logoutButton.grid(row=0, column=1, columnspan=3, sticky="ne")
        self.songSelect = SongSelect(self, self.library, self.player)
        self.songSelect.grid(row=0, column=0, rowspan=3, sticky="nsew")

    def showLoginScreen(self):
        self.login = Login(self, self.db)
        self.login.lift()
        self.login.grab_set()

    def logOutUser(self):
        self.db.logOutUser()
        self.showLoginScreen()

    # def changeCurrentSong(self):


if __name__ == "__main__":
    app = App()
    app.mainloop()
