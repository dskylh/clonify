import sqlite3
from tkinter import filedialog, messagebox
from typing import Optional

from customtkinter import CTkLabel, CTkButton, CTkFrame, CTkInputDialog, CTkToplevel
from music import Music
from player import Player
from db import DbConnection

from sptpy import search_music


def music_by_hand(file_path) -> Optional[Music]:
    if type(file_path) is tuple:
        # if file_path is actually a tuple then no file was selected
        print("Dosya Secilmedi")
        return
    music_info = "Muzik Bilgileri"
    music_name = CTkInputDialog(
        text="Muzigin Ismini Giriniz (Zorunlu)", title=music_info
    ).get_input()
    while music_name == "" or music_name is None or music_name.isspace():
        music_name = CTkInputDialog(
            text="Muzigin Ismini Giriniz (Zorunlu)", title=music_info
        ).get_input()
    artist = CTkInputDialog(
        text="Muzigin Sanatcisini Giriniz", title=music_info
    ).get_input()
    album = CTkInputDialog(
        text="Muzigin Albumunu Giriniz", title=music_info
    ).get_input()
    genre = CTkInputDialog(text="Muzigin Turunu Giriniz", title=music_info).get_input()
    music = Music(music_name, file_path, artist, album, genre)
    return music


class SongSelect(CTkFrame):
    def __init__(self, master, player: Player, db: DbConnection):
        super().__init__(master)
        self.main_window = master
        self.currentMusic = None
        self.player = player
        self.db = db
        self.library = self.db.get_musics("")
        self.show_music_buttons()

    def changeCurrentMusic(self, music: Music):
        self.main_window.currentMusic = music
        self.player.library = self.library
        self.player.current = music
        self.player.play_music()
        self.main_window.albumCover()

    def show_music_buttons(self):
        for widget in self.winfo_children():
            widget.destroy()
        add_music_button = CTkButton(self, text="Sarki ekle", command=self.open_music)
        # add_music_button.grid(row=0, column=0, padx=2.5, pady=2.5, sticky="wne")
        add_music_button.pack(pady=5, padx=2.5)
        self.library = self.db.get_musics("")

        for music, rowcount in zip(self.library, range(len(self.library))):
            if music.music_name is None:
                info_label = CTkLabel(self, text="Kütüphanenizde Hiç Şarkı Yok")
                # info_label.grid(row=1, column=0, padx=2.5, pady=2.5, sticky="wn")
                info_label.pack(padx=2.5)
                return
            # CTkButton(master=self, text=music.music_name + ", " + music.artist,
            #           command=lambda m=music: self.changeCurrentMusic(m)).grid(row=rowcount, pady=2.5)
            CTkButton(
                master=self,
                text=music.music_name + ", " + music.artist,
                command=lambda m=music: self.changeCurrentMusic(m),
                fg_color="#2b2b2b",
            ).pack(pady=2.5, padx=2.5)

    def open_music(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Music Files", "*.mp3 *.ogg .wav .flac")]
        )
        # music = music_by_hand(file_path)
        music = search_music(file_path)
        if music is None:
            return
        try:
            self.db.add_music(music)
        except sqlite3.Error as error:
            if error.sqlite_errorcode == 2067:
                messagebox.showerror(
                    "Baska bir muzik seciniz.",
                    "Bu muzik zaten veri tabaninda mevcuttur.",
                )
        self.show_music_buttons()
