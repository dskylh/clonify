from customtkinter import CTkOptionMenu
from user import User


class UserMenu(CTkOptionMenu):
    def __init__(self, main_window, user: User):
        super().__init__(main_window, command=self.option_menu_callback)
        self.main_window = main_window
        self.CIKIS = "Çıkış Yap"
        if user.user_name is None:
            self.set("Giriş Yapılmadı")
            self.configure(values=[self.CIKIS])
        else:
            self.set(user.user_name)
            self.configure(values=[self.CIKIS])

    def option_menu_callback(self, choice):
        if choice == self.CIKIS:
            self.main_window.logOutUser()
            self.main_window.player.stop_music()
