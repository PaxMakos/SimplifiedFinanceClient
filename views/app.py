from customtkinter import *
from tkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()

        self.currentUi = []

        self.title("Finance Manager")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.geometry(f"{screen_width}x{screen_height}+0+0")

        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
