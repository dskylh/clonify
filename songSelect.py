from music import Music
from customtkinter import *


class songSelect(CTkFrame):
    def __init__(self, mainWindow, musicList: list[Music]):
        super().__init__(mainWindow)
        self.currentMusic = None
        for music in musicList:
            self.button = CTkButton(
                master=self,
                text=music.musicName + ", " + music.artist,
                command=lambda m=music: self.changeCurrentMusic(m),
            ).pack(side="top", fill="x")

    def changeCurrentMusic(self, music: Music):
        self.currentMusic = music
