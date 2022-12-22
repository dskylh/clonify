from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel, CTkSlider
from PIL import Image, ImageTk
from player import Player
from pygame import mixer_music

import tkinter as tk


class PlayerUi(CTkFrame):
    def __init__(self, master, player: Player):
        super().__init__(master)
        self.player = player
        self.configure(corner_radius=0)
        self.main_window = master

        play_button_image_pil = Image.open("img/play_button.png")
        self.play_button_image = CTkImage(
            dark_image=play_button_image_pil, size=(40, 40)
        )

        pause_button_image_pil = Image.open("img/pause_button.png")
        self.pause_button_image = CTkImage(
            dark_image=pause_button_image_pil, size=(40, 40)
        )

        self.play_button = CTkButton(
            self,
            image=self.play_button_image,
            text="",
            width=40,
            height=40,
            fg_color="#2b2b2b",
            hover=False,
        )

        # if the button isn't initialized then it gives an error so i added the command after it
        self.play_button.configure(command=self.play_pause)
        self.play_button.grid(row=0, column=0, sticky="e")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.slider = CTkSlider(
            master=self,
            from_=0,
            to=int(self.player.current_duration),
            command=self.song_slider,
        )

        self.next_button = CTkButton(
            self,
            text="next",
            width=40,
            height=40,
            fg_color="#2b2b2b",
            hover=False,
            command=self.play_next,
        )
        self.next_button.grid(row=0, column=1, sticky="w")
        self.columnconfigure(1, weight=1)

        self.slider.set(self.player.get_cur_pos())
        self.slider.grid(row=1, column=0, columnspan=2, pady=5, sticky="we")
        self.rowconfigure(1, weight=1)

        min, secs = divmod(int(self.player.current_duration), 60)
        min_cur, secs_cur = divmod(int(self.player.get_cur_pos()), 60)
        # print(min_cur, secs_cur)

        self.duration_label = CTkLabel(self, text=f"{min_cur}:{secs_cur}/{min}:{secs}")
        self.duration_label.grid(row=1, column=2, sticky="e", padx=10)

        # self.rowconfigure(1, weight=2)

    def play_pause(self):
        self.player.play_music()
        cur_image_button = self.play_button.cget("image")
        if cur_image_button is self.play_button_image:
            self.play_button.configure(image=self.pause_button_image)
        else:
            self.play_button.configure(image=self.play_button_image)

        self.song_slider(self.slider.get())

    def play_next(self):
        self.player.next_music()
        self.player.update_current_duration()
        self.player.is_playing = False
        self.player.play_music()
        self.player.update_current_duration()
        self.main_window.albumCover()
        player_ui = self.main_window.player_ui
        player_ui.song_slider(player_ui.slider.get())

    def song_slider(self, value):
        self.slider.configure(to=int(self.player.current_duration))
        cur_pos = self.player.get_cur_pos()
        self.slider.set(cur_pos)
        self.update_duration_label()
        if self.player.get_busy():
            self.after(100, lambda: self.song_slider(self.slider.get()))

    def update_duration_label(self):
        min, secs = divmod(int(self.player.current_duration), 60)
        min_cur, secs_cur = divmod(int(self.player.get_cur_pos()), 60)
        self.duration_label.configure(text=f"{min_cur}:{secs_cur}/{min}:{secs}")
