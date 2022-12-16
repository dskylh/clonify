from customtkinter import (
    END,
    CTk,
    CTkButton,
    CTkEntry,
    CTkLabel,
    CTkToplevel,
    StringVar,
)
from db import DbConnection, User
from sqlite3 import Error as SqError
import time


class Login(CTkToplevel):
    def __init__(self, mainWindow: CTk, db: DbConnection):
        super().__init__(mainWindow)
        self.db = db

        self.title("Giriş")

        self.minsize(350, 250)

        self.loggedInUser = db.getLoggedInUser()

        self.username = StringVar()
        self.password = StringVar()

        self.usernameLabel = CTkLabel(self, text="Kullanıcı Adı:")
        self.usernameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.passwordLabel = CTkLabel(self, text="Şifre:")
        self.passwordLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.usernameEntry = CTkEntry(self, textvariable=self.username)
        self.usernameEntry.grid(row=0, column=1, padx=10, sticky="w")

        self.passwordEntry = CTkEntry(self, textvariable=self.password)
        self.passwordEntry.grid(row=1, column=1, padx=10, sticky="w")

        self.loginButton = CTkButton(self, text="Giriş yap", command=self.login)
        self.loginButton.grid(row=2, columnspan=2, padx=10, pady=5, sticky="we")

        self.registerButton = CTkButton(self, text="Kayit ol", command=self.register)
        self.registerButton.grid(row=3, columnspan=2, padx=10, pady=5, sticky="we")

        self.infoLabel = CTkLabel(self, text="")
        self.protocol("WM_DELETE_WINDOW", lambda: None)
        self.grab_set()

    def login(self):
        try:
            if (
                self.username.get().isspace()
                or self.passwordEntry.get().isspace()
                or self.username.get().strip() == ""
                or self.password.get().strip() == ""
            ):
                self.infoLabel.configure(
                    text="Bos kullanici adi veya sifre girmeyiniz."
                )
                return

            if self.loggedInUser.userName is not None:
                print("A user is already logged in")
                return
            user = self.db.getUser(self.username.get())
            assert user.userName is not None
            passcheck = user.checkPassword(self.password.get())
            if not passcheck:
                self.infoLabel.configure(text="Sifreniz yanlis!")
            else:
                self.db.changeUserLoggedIn(user)
                self.infoLabel.configure(text="Giris basarili!")

        except AssertionError:
            self.infoLabel.configure(text="Kullanici adinizi kontrol ediniz.")

        except SqError:
            print("Error occured while connecting to the database: ", SqError)
            self.infoLabel.configure(
                text="Veri tabanına bağlanırken bir problem yaşandı"
            )

        finally:
            self.loggedInUser = self.db.getLoggedInUser()
            self.infoLabel.grid(
                row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we"
            )
            if self.loggedInUser.userName is not None:
                self.after(2000, self.destroy)

    def register(self):
        try:
            username = self.username.get()
            password = self.password.get()
            user = self.db.getUser(username)
            if user.userName is None:
                user = User(username, password)
                self.db.addUser(user)
                self.infoLabel.configure(text="yeni kullanici olusturulmustur.")
                self.usernameEntry.delete(0, END)
                self.passwordEntry.delete(0, END)
            else:
                self.infoLabel.configure(text="Bu kullanici adi zaten kayitli.")
        except SqError:
            print("Error occured while connecting to the database: ", SqError)
            self.infoLabel.configure(
                text="Veri tabanına bağlanırken bir problem yaşandı"
            )
        finally:
            self.infoLabel.grid(
                row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we"
            )
