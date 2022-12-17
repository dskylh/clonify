from music import Music
from player import Player
import customtkinter


class SongSelect(customtkinter.CTkFrame):
    def __init__(self, main_window, music_list: list[Music], player: Player):
        super().__init__(main_window)
        self.mainWindow = main_window
        self.currentMusic = None
        self.player = player
        for music, rowcount in zip(music_list, range(len(music_list))):
            self.button = customtkinter.CTkButton(
                master=self,
                text=music.music_name + ", " + music.artist,
                command=lambda m=music: self.changeCurrentMusic(m),
            ).grid(row=rowcount, pady=2.5)

    def changeCurrentMusic(self, music: Music):
        self.mainWindow.currentMusic = music
        self.player.current = music
        self.player.play_music()
