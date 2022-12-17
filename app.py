import customtkinter
from SongSelect import SongSelect
from db import DbConnection
from login import Login
from player import Player
from music import Music
from typing import Optional


class App(customtkinter.CTk):
    """
    The main application class
    """
    def __init__(self):
        super().__init__()
        self.db = DbConnection()
        self.library = self.db.get_musics("")
        self.player = Player(library=self.library)
        self.loggedInUser = self.db.get_logged_in_user()
        self.currentMusic: Music
        print(self.loggedInUser.user_name)
        self.login: Optional[Login] = None
        if self.loggedInUser.user_name is None:
            self.login = Login(self, self.db)
            self.login.grab_set()
        print(self.login)
        self.musicNameList = [music.music_name for music in self.library]
        self.logoutButton = customtkinter.CTkButton(self, text="Log Out", command=self.logOutUser)

        self.logoutButton.grid(row=0, column=1, columnspan=3, sticky="ne")
        self.songSelect = SongSelect(self, self.library, self.player)
        self.songSelect.grid(row=0, column=0, rowspan=3, sticky="nsew")

    def showLoginScreen(self):
        """
        Shows the login screen after a logout
        :return: None
        """
        self.login = Login(self, self.db)
        self.login.lift()
        self.login.grab_set()

    def logOutUser(self):
        """
        Logs out the user
        :return:
        """
        self.db.log_out_user()
        self.showLoginScreen()


if __name__ == "__main__":
    app = App()
    app.mainloop()
