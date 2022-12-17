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


class Login(CTkToplevel):
    """
    A top level window for users to login.
    """
    def __init__(self, main_window: CTk, db: DbConnection):
        """
        Creates the window's widgets
        :param main_window:
        :param db:
        """
        super().__init__(main_window)
        self.db = db

        self.title("Giriş")

        self.minsize(350, 250)

        self.logged_in_user = db.get_logged_in_user()

        self.username = StringVar()
        self.password = StringVar()

        self.username_label = CTkLabel(self, text="Kullanıcı Adı:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.password_label = CTkLabel(self, text="Şifre:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.username_entry = CTkEntry(self, textvariable=self.username)
        self.username_entry.grid(row=0, column=1, padx=10, sticky="w")

        self.password_entry = CTkEntry(self, textvariable=self.password)
        self.password_entry.grid(row=1, column=1, padx=10, sticky="w")

        self.login_button = CTkButton(self, text="Giriş yap", command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=5, sticky="we")

        self.register_button = CTkButton(self, text="Kayit ol", command=self.register)
        self.register_button.grid(row=3, columnspan=2, padx=10, pady=5, sticky="we")

        self.info_label = CTkLabel(self, text="")
        self.protocol("WM_DELETE_WINDOW", lambda: None)
        self.wm_attributes("-topmost", True)

    def login(self):
        """
        Logs a user in and changes the current logged-in user.
        :return:
        """
        try:
            if (
                    self.username.get().isspace()
                    or self.password_entry.get().isspace()
                    or self.username.get().strip() == ""
                    or self.password.get().strip() == ""
            ):
                self.info_label.configure(
                    text="Bos kullanici adi veya sifre girmeyiniz."
                )
                return

            if self.logged_in_user.user_name is not None:
                print("A user is already logged in")
                return
            user = self.db.get_user(self.username.get())
            assert user.user_name is not None
            pass_check = user.check_password(self.password.get())
            if not pass_check:
                self.info_label.configure(text="Sifreniz yanlis!")
            else:
                self.db.change_user_logged_in(user)
                self.info_label.configure(text="Giris basarili!")

        except AssertionError:
            self.info_label.configure(text="Kullanici adinizi kontrol ediniz.")

        except SqError:
            print("Error occured while connecting to the database: ", SqError)
            self.info_label.configure(
                text="Veri tabanına bağlanırken bir problem yaşandı"
            )

        finally:
            self.logged_in_user = self.db.get_logged_in_user()
            self.info_label.grid(
                row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we"
            )
            if self.logged_in_user.user_name is not None:
                self.after(700, self.destroy)

    def register(self):
        """
        Registers a user into the database
        :return:
        """
        try:
            if (
                    self.username.get().isspace()
                    or self.password_entry.get().isspace()
                    or self.username.get().strip() == ""
                    or self.password.get().strip() == ""
            ):
                self.info_label.configure(
                    text="Bos kullanici adi veya sifre girmeyiniz."
                )
                return
            username = self.username.get()
            password = self.password.get()
            user = self.db.get_user(username)
            if user.user_name is None:
                user = User(username, password)
                self.db.adduser(user)
                self.info_label.configure(text="yeni kullanici olusturulmustur.")
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
            else:
                self.info_label.configure(text="Bu kullanici adi zaten kayitli.")
        except SqError:
            print("Error occured while connecting to the database: ", SqError)
            self.info_label.configure(
                text="Veri tabanına bağlanırken bir problem yaşandı"
            )
        finally:
            self.info_label.grid(
                row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we"
            )
