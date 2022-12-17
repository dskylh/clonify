from music import Music
from player import Player
import customtkinter


class SongSelect(customtkinter.CTkFrame):
    def __init__(self, mainwindow, musiclist: list[Music], player: Player):
        super().__init__(mainwindow)
        self.mainWindow = mainwindow
        self.currentMusic = None
        self.player = player

        for music, rowcount in zip(musiclist, range(len(musiclist))):
            self.button = customtkinter.CTkButton(
                master=self,
                text=music.musicName + ", " + music.artist,
                command=lambda m=music: self.changeCurrentMusic(m),
            ).grid(row=rowcount, pady=2.5)

    def changeCurrentMusic(self, music: Music):
        self.mainWindow.currentMusic = music
        self.player.current = music
        self.player.playMusic()
