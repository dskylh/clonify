from customtkinter import CTkOptionMenu
from user import User


class UserMenu(CTkOptionMenu):
    def __init__(self, main_window, user: User):
        super().__init__(main_window, command=self.option_menu_callback)
        self.main_window = main_window
        if user.user_name is None:
            self.set("Giriş Yapılmadı")
        else:
            self.set(user.user_name)
            self.configure(values=["Çıkış Yap"])

    def option_menu_callback(self, choice):
        if choice == "Çıkış Yap":
            self.main_window.logOutUser()
