from customtkinter import CTkButton, CTkFrame, CTkImage
from PIL import Image, ImageTk
from player import Player
from pygame import mixer_music

import tkinter as tk


class PlayerUi(CTkFrame):
    def __init__(self, master, player: Player):
        super().__init__(master)
        self.player = player

        play_button_image_pil = Image.open("img/play_button.png")
        self.play_button_image = CTkImage(dark_image=play_button_image_pil, size=(40, 40))

        pause_button_image_pil = Image.open("img/pause_button.png")
        self.pause_button_image = CTkImage(dark_image=pause_button_image_pil, size=(40, 40))

        self.play_button = CTkButton(self, image=self.play_button_image, text="", width=40, height=40,
                                     fg_color="#2b2b2b", hover=False)

        # if the button isn't initialized then it gives an error so i added the command after it
        self.play_button.configure(command=self.play_pause)
        self.play_button.grid(row=0, column=0, sticky="e")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def play_pause(self):
        self.player.play_music()
        cur_image_button = self.play_button.cget("image")
        if cur_image_button is self.play_button_image:
            self.play_button.configure(image=self.pause_button_image)
        else:
            self.play_button.configure(image=self.play_button_image)
