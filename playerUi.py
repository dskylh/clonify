from customtkinter import CTkButton, CTkFrame, CTkImage
from PIL import Image, ImageTk
from player import Player

import tkinter as tk


class PlayerUi(CTkFrame):
    def __init__(self, master, player: Player):
        super().__init__(master)
        self.player = player
        play_button_image_pil = Image.open("img/play_button.png")
        play_button_image = CTkImage(dark_image=play_button_image_pil, size=(40, 40))

        play_button_image = CTkImage(dark_image=play_button_image_pil)

        play_button = CTkButton(
            self,
            image=play_button_image,
            text="",
            width=40,
            height=40,
            fg_color="#2b2b2b",
            command=player.play_music,
        )
        play_button.grid(row=0, column=0, rowspan=2, sticky="s")
