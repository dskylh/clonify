from customtkinter import CTkLabel, CTkButton, CTkFrame, CTkScrollbar
import tkinter

from music import Music
from player import Player


class SongSelect(CTkFrame):
    def __init__(self, main_window, music_list: list[Music], player: Player):
        super().__init__(main_window)
        self.mainWindow = main_window
        self.currentMusic = None
        self.player = player
        rowcount = 0
        for music, rowcount in zip(music_list, range(len(music_list))):
            if music.music_name is None:
                self.info_label = CTkLabel(text="Kütüphanenizde Hiç Şarkı Yok")
                self.info_label.grid(row=0, column=0, padx=2.5, pady=2.5, sticky="w")
                return
            self.button = CTkButton(
                master=self,
                text=music.music_name + ", " + music.artist,
                command=lambda m=music: self.changeCurrentMusic(m),
            ).grid(row=rowcount, pady=2.5)

    def changeCurrentMusic(self, music: Music):
        self.mainWindow.currentMusic = music
        self.player.current = music
        self.player.play_music()
