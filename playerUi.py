from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel, CTkSlider
from PIL import Image
from player import Player


class PlayerUi(CTkFrame):
    def __init__(self, master, player: Player):
        super().__init__(master)
        self.player = player
        self.configure(corner_radius=0)
        self.main_window = master

        play_button_image_pil = Image.open("img/play_button.png")
        self.play_button_image = CTkImage(dark_image=play_button_image_pil, size=(40, 40))

        pause_button_image_pil = Image.open("img/pause_button.png")
        self.pause_button_image = CTkImage(dark_image=pause_button_image_pil, size=(40, 40))

        self.play_button = CTkButton(self, image=self.play_button_image, text="", width=40, height=40,
                                     fg_color="#2b2b2b", hover=False, )

        # if the button isn't initialized then it gives an error, so I added the command after it
        self.play_button.configure(command=self.play_pause)
        self.play_button.grid(row=0, column=1, sticky="")
        self.rowconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)

        previous_button_image_pil = Image.open("img/previous_button.png")
        self.previous_button_image = CTkImage(dark_image=previous_button_image_pil, size=(40, 40))
        self.previous_button = CTkButton(self, image=self.previous_button_image, text="", width=40, height=40,
                                         fg_color="#2b2b2b", hover=False,
                                         command=self.play_previous, )

        self.previous_button.grid(row=0, column=0, sticky="e")
        self.columnconfigure(0, weight=1)

        next_button_image_pil = Image.open("img/next_button.png")
        self.next_button_image = CTkImage(dark_image=next_button_image_pil, size=(40, 40))
        self.next_button = CTkButton(self, image=self.next_button_image, text="", width=40, height=40,
                                     fg_color="#2b2b2b", hover=False,
                                     command=self.play_next, )
        self.next_button.grid(row=0, column=2, sticky="w")
        self.columnconfigure(2, weight=1)

        self.volume_slider = CTkSlider(master=self, from_=0, to=100, orientation="vertical", height=50,
                                       command=self.set_volume, )

        self.volume_slider.grid(row=0, column=4, rowspan=2, sticky="ns", padx=2)

        self.slider = CTkSlider(master=self, from_=0, to=int(self.player.current_duration), command=self.song_slider, )

        self.slider.set(self.player.get_cur_pos())
        self.slider.grid(row=1, column=0, columnspan=3, pady=5, sticky="we")
        self.rowconfigure(1, weight=1)

        minute, secs = divmod(int(self.player.current_duration), 60)
        min_cur, secs_cur = divmod(int(self.player.get_cur_pos()), 60)

        self.duration_label = CTkLabel(self, text=f"{min_cur}:{secs_cur}/{minute}:{secs}")
        self.duration_label.grid(row=1, column=3, sticky="e", padx=10)

        # self.rowconfigure(1, weight=2)

    def play_pause(self):
        self.player.play_music()
        cur_image_button = self.play_button.cget("image")

        if cur_image_button is self.play_button_image:
            self.play_button.configure(image=self.pause_button_image)
        else:
            self.play_button.configure(image=self.play_button_image)

        self.song_slider(self.slider.get())

    def update_ui(self):
        self.player.update_current_duration()
        self.player.is_playing = False
        self.player.play_music()
        self.player.update_current_duration()
        self.main_window.albumCover()
        self.song_slider(self.slider.get())
        if self.player.get_busy():
            self.play_button.configure(image=self.pause_button_image)
        else:
            self.play_button.configure(image=self.play_button_image)

    def play_next(self):
        self.player.next_music()
        self.update_ui()

    def play_previous(self):
        self.player.previous_music()
        self.update_ui()

    def song_slider(self, value):
        self.slider.configure(to=int(self.player.current_duration))
        cur_pos = self.player.get_cur_pos()
        self.slider.set(cur_pos)
        self.update_duration_label()
        if self.player.get_busy():
            self.after(100, lambda: self.song_slider(self.slider.get()))

    def update_duration_label(self):
        minute, secs = divmod(int(self.player.current_duration), 60)
        min_cur, secs_cur = divmod(int(self.player.get_cur_pos()), 60)
        self.duration_label.configure(text=f"{min_cur}:{secs_cur}/{minute}:{secs}")

    def set_volume(self, value):
        self.player.set_music_vol(value)
