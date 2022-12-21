import customtkinter
import tkinter as tk
from SongSelect import SongSelect
from db import DbConnection
from login import Login
from player import Player
from music import Music
from sptpy import search_cover
from userMenu import UserMenu
from fileMenu import FileMenu
from playerUi import PlayerUi
from PIL import Image
import requests
import io


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
        self.minsize(width=750, height=500)
        if self.loggedInUser.user_name is None:
            self.login = Login(self, self.db)
            self.login.grab_set()
        self.musicNameList = [music.music_name for music in self.library]
        self.songSelect = SongSelect(self, self.player, self.db)
        self.songSelect.grid(row=0, column=0, rowspan=2, sticky="nswe")
        self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        self.user_menu_var = customtkinter.StringVar()
        self.user_menu = UserMenu(
            self, self.loggedInUser, self.option_menu_callback, self.user_menu_var
        )
        self.user_menu.grid(row=0, column=3, sticky="ne")
        self.columnconfigure(3, weight=2)
        self.player_ui = PlayerUi(self, self.player)
        self.player_ui.grid(row=1, column=2, columnspan=2, sticky="nsew")
        self.columnconfigure(2, weight=1)
        self.albumCover()

    def showLoginScreen(self):
        """
        Shows the login screen after a logout
        :return: None
        """
        self.login = Login(self, self.db)
        self.login.lift()
        self.login.grab_set()
        self.user_menu.set(self.loggedInUser.user_name)

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
        self.user_menu.set("Giris Yapilmadi")

    def albumCover(self):
        response = requests.get(search_cover(self.player.current))
        data = response.content
        file = io.BytesIO(data)

        self.cover_image = Image.open(file)
        cover_image = customtkinter.CTkImage(
            dark_image=self.cover_image, size=(300, 300)
        )
        self.cover_image_label = customtkinter.CTkLabel(
            self, image=cover_image, text="", height=300, width=300
        )
        self.cover_image_label.grid(row=0, column=1, columnspan=2, sticky="e")


if __name__ == "__main__":
    app = App()
    app.mainloop()
