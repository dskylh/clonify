from customtkinter import *
from db import DbConnection


class Login(CTk):
    def __init__(self):
        super().__init__()

        self.title("Clonify")
        self.minsize(300, 200)
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")
        self.grid_rowconfigure(weight=2, index=0)
        self.userNameEntry = CTkEntry(master=self, placeholder_text="Kullanıcı adı")
        self.passwordEntry = CTkEntry(master=self, placeholder_text="Şifre")
        self.loginButton= CTkButton(master=self, command=self.login, text="Giris Yap")
        self.registerButton= CTkButton(master=self, command=self.login, text="Kayit Ol")

        self.sqlcon = DbConnection()

        self.userNameEntry.grid(row=0, column=0, padx=20, pady=15)
        self.passwordEntry.grid(row=1, column=0, padx=20, pady=15)
        self.loginButton.grid(row=2, column=0, padx=20, pady=15)
        self.registerButton.grid(row=2, column=1, padx=20, pady=15)

    def login(self):
        user = self.sqlcon.getUser(self.userNameEntry.get())
        print(user.password)

    # def



if __name__ == "__main__":
    app = Login()
    app.mainloop()
