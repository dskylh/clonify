from customtkinter import CTkOptionMenu
from user import User


class UserMenu(CTkOptionMenu):
    def __init__(self, main_window, user: User, command):
        super().__init__(main_window, command=command)
        if user.user_name is None:
            self.set("Giriş Yapılmadı")
        else:
            self.set(user.user_name)
            self.configure(values=[user.user_name, "Çıkış Yap"])

    def update_value(self, user: User):
        if user.user_name is None:
            self.set("Giriş Yapılmadı")
        else:
            self.set(user.user_name)
            self.configure(values=[user.user_name, "Çıkış Yap"])
