from customtkinter import *

from db import DbConnection
from login import Login
from player import Player


class App(CTk):
    def __init__(self):
        super().__init__()
        self.db = DbConnection()
        self.library = self.db.getMusics("")
        self.player = Player(library=self.library)
        self.loggedInUser = self.db.getLoggedInUser()
        print(self.loggedInUser.userName)
        if self.loggedInUser.userName is None:
            self.showLoginScreen()

        self.musicNameList = [music.musicName for music in self.library]
        self.songOptionMenu = CTkOptionMenu(
            master=self, values=self.musicNameList, command=self.changeCurrentSong
        )
        self.songButton = CTkButton(self, text="Song", command=self.player.playMusic)
        self.logoutButton = CTkButton(self, text="Log Out", command=self.logOutUser)

        self.songButton.pack()
        self.songOptionMenu.pack()
        self.logoutButton.pack()

    def showLoginScreen(self):
        login = Login(self, self.db).loggedInUser
        print(login.userName)

    def logOutUser(self):
        self.db.logOutUser()
        self.showLoginScreen()

    def changeCurrentSong(self, choice):
        for music in self.library:
            if music.musicName == choice:
                self.player.current = music
                break


if __name__ == "__main__":
    app = App()
    app.mainloop()
