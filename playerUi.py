from customtkinter import CTkButton, CTkFrame, CTkImage
from PIL import Image

# import tkinter as tk


class PlayerUi(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        play_button_image_pil = Image.open(fp="img/play_button.png")
        play_button_image = CTkImage(dark_image=play_button_image_pil)

        play_button = CTkButton(self, image=play_button_image)
        play_button.pack()
