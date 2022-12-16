from music import Music
from player import Player
from customtkinter import *


class songSelect(CTkFrame):
    def __init__(self, mainWindow, musicList: list[Music], player: Player):
        super().__init__(mainWindow)
        self.mainWindow = mainWindow
        self.currentMusic = None
        self.player = player

        for music, rowcount in zip(musicList, range(len(musicList))):
            self.button = CTkButton(
                master=self,
                text=music.musicName + ", " + music.artist,
                command=lambda m=music: self.changeCurrentMusic(m),
            ).grid(row=rowcount, pady=2.5)

    def changeCurrentMusic(self, music: Music):
        self.mainWindow.currentMusic = music
        self.player.current = music
        print(self.mainWindow.currentMusic.musicName)
