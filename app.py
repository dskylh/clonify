import customtkinter
from SongSelect import SongSelect
from db import DbConnection
from login import Login
from player import Player
from music import Music
from userMenu import UserMenu
from fileMenu import FileMenu


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
        self.login = None
        if self.loggedInUser.user_name is None:
            self.login = Login(self, self.db)
            self.login.grab_set()
        self.musicNameList = [music.music_name for music in self.library]
        self.songSelect = SongSelect(self, self.library, self.player)
        self.songSelect.grid(row=0, column=0, sticky="nsw")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.user_menu = UserMenu(self, self.loggedInUser, self.option_menu_callback)
        self.user_menu.grid(row=0, column=1, sticky="ne")

    def showLoginScreen(self):
        """
        Shows the login screen after a logout
        :return: None
        """
        self.login = Login(self, self.db)
        self.login.lift()
        self.login.grab_set()
        self.user_menu.update_value(self.loggedInUser)

    def option_menu_callback(self, choice):
        if choice == "Çıkış Yap":
            self.logOutUser()

    def logOutUser(self):
        """
        Logs out the user
        :return:
        """
        self.db.log_out_user()
        self.showLoginScreen()
        self.user_menu.update_value(self.loggedInUser)


if __name__ == "__main__":
    app = App()
    app.mainloop()
