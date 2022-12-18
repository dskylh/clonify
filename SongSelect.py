from tkinter import filedialog
from customtkinter import CTkLabel, CTkButton, CTkFrame, CTkScrollbar
import tkinter
from music import Music
from player import Player
import os


class SongSelect(CTkFrame):
    def __init__(self, main_window, music_list: list[Music], player: Player):
        super().__init__(main_window)
        self.mainWindow = main_window
        self.currentMusic = None
        self.player = player
        self.library = music_list
        self.show_music_buttons()
        self.file_path = tkinter.StringVar()

    def changeCurrentMusic(self, music: Music):
        self.mainWindow.currentMusic = music
        self.player.current = music
        self.player.play_music()

    def show_music_buttons(self):
        for widget in self.winfo_children():
            widget.destroy()
        add_music_button = CTkButton(self, text="Sarki ekle",
                                     command=lambda: self.file_path.set(self.return_file_path()))
        add_music_button.grid(row=0, column=0, padx=2.5, pady=2.5, sticky="wne")

        for music, rowcount in zip(self.library, range(len(self.library))):
            if music.music_name is None:
                info_label = CTkLabel(self, text="Kütüphanenizde Hiç Şarkı Yok")
                info_label.grid(row=1, column=0, padx=2.5, pady=2.5, sticky="wn")
                return
            CTkButton(master=self, text=music.music_name + ", " + music.artist,
                      command=lambda m=music: self.changeCurrentMusic(m), ).grid(row=rowcount, pady=2.5)

    def return_file_path(self):
        file_path = filedialog.askopenfilename()
        self.show_music_buttons()
        music_name = os.path.splitext(os.path.basename(file_path))[0]
        return file_path
