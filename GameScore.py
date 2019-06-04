from tkinter import *


class GameScore:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x200")

        self.frame = Frame(self.master, width=400, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.frame.pack(fill="both", expand=True)
