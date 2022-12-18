from typing import Optional

import customtkinter

import tkinter as tk
from tkinter import filedialog

from music import Music


def return_file_path():
    file_path = filedialog.askopenfilename()
    return file_path


class FileMenu(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        self.file_menu = tk.Menu(self)
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_path = customtkinter.StringVar()
        self.file_menu.add_command(label="Open Music", command=lambda: self.file_path.set(return_file_path()))

    def music(self) -> Optional[Music]:
        file_path = self.file_path.get()
        if file_path is None or file_path == "":
            return None





