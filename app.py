from customtkinter import *
from songSelect import songSelect

from db import DbConnection
from login import Login
from player import Player
from music import Music


class App(CTk):
    def __init__(self):
        super().__init__()
        self.db = DbConnection()
        self.library = self.db.getMusics("")
        self.player = Player(library=self.library)
        self.loggedInUser = self.db.getLoggedInUser()
        self.currentMusic: Music
        print(self.loggedInUser.userName)
        if self.loggedInUser.userName is None:
            self.showLoginScreen()

        self.musicNameList = [music.musicName for music in self.library]
        # self.songOptionMenu = CTkOptionMenu(
        #     master=self, values=self.musicNameList, command=self.changeCurrentSong
        # )
        self.songButton = CTkButton(self, text="Song", command=self.player.playMusic)
        self.logoutButton = CTkButton(self, text="Log Out", command=self.logOutUser)

        self.logoutButton.grid(row=0, column=1, columnspan=3, sticky="nswe")
        self.songButton.grid(row=1, column=1, columnspan=3, sticky="nswe")
        self.songSelect = songSelect(self, self.library, self.player)
        self.songSelect.grid(row=0, column=0, rowspan=3, sticky="nsew")

    def showLoginScreen(self):
        Login(self, self.db).deiconify()

    def logOutUser(self):
        self.db.logOutUser()
        self.showLoginScreen()

    # def changeCurrentSong(self):


if __name__ == "__main__":
    app = App()
    app.mainloop()
