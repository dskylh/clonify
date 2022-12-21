from customtkinter import CTkButton, CTkFrame, CTkImage
from PIL import Image, ImageTk
from player import Player

import tkinter as tk


class PlayerUi(CTkFrame):
    def __init__(self, master, player: Player):
        super().__init__(master)
        self.player = player
        play_button_image_pil = Image.open("img/play_button.png")
        self.play_button_image = CTkImage(
            dark_image=play_button_image_pil, size=(40, 40)
        )
        pause_button_image_pil = Image.open("img/pause_button.png")
        self.pause_button_image = CTkImage(
            dark_image=pause_button_image_pil, size=(40, 40)
        )

        # play_button_image = CTkImage(dark_image=play_button_image_pil)

        self.play_button = CTkButton(
            self,
            image=self.play_button_image,
            text="",
            width=40,
            height=40,
            fg_color="#2b2b2b",
            command=self.player.play_music,
        )
        self.play_button.grid(row=0, column=0, sticky="e")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.pause_button = CTkButton(
            self,
            image=self.pause_button_image,
            text="",
            width=40,
            height=40,
            fg_color="#2b2b2b",
            command=self.player.pause_music,
        )
        self.pause_button.grid(row=0, column=1, sticky="w")
        self.columnconfigure(1, weight=1)
