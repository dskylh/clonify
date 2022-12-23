from customtkinter import CTkOptionMenu
from customtkinter.windows import CTkInputDialog


class SearchMusic(CTkOptionMenu):
    def __init__(self, main_window):
        super().__init__(main_window, command=self.option_menu_callback)
        self.main_window = main_window
        self.db = self.main_window.db
        self.configure(values=["Müzik", "Albüm", "Sanatçı", "Sıfırla"], anchor="center")
        self.set("Arama")

    def option_menu_callback(self, choice):
        self.set("Arama")
        if choice == "Sıfırla":
            library = self.db.get_musics("")
        else:
            dialog = CTkInputDialog(text=f"{choice} ara", title="Arama")
            library = self.db.get_musics(dialog.get_input(), search_type=choice)
        self.main_window.library = library
        self.main_window.show_music_buttons()
