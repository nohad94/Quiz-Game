from tkinter import *
from Question import *
from Game import *
from Option import *
from HighScore import *

APP_NAME = "Quiz Game"


class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x700")

        self.frame = Frame(self.master, width=500, height=500, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.frame.pack(fill="both", expand=True)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)
        self.frame.rowconfigure(4, weight=0)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=0)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=0)
        self.frame.columnconfigure(3, weight=1)

        self.title = Label(self.frame, width=35, height=10, text="Quiz Game", font="times 19")
        self.title.grid(row=0, column=0, columnspan=5, rowspan=2, sticky="nsew")

        self.empty_frame1 = Label(self.frame, width=10, height=10)
        self.empty_frame1.grid(row=2, column=1, rowspan=5, sticky="nsew")
        self.empty_frame2 = Label(self.frame, width=10, height=10)
        self.empty_frame2.grid(row=2, column=3, rowspan=5, sticky="nsew")

        self.button_label1 = Label(self.frame, width=25, height=25, borderwidth=2, relief="raised")
        self.button_label1.grid(row=2, column=2, sticky="nsew")
        self.button_label2 = Label(self.frame, width=25, height=25, borderwidth=2, relief="raised")
        self.button_label2.grid(row=3, column=2, sticky="nsew")
        self.button_label3 = Label(self.frame, width=25, height=25, borderwidth=2, relief="raised")
        self.button_label3.grid(row=4, column=2, sticky="nsew")
        self.empty_label = Label(self.frame, width=25, height=25)
        self.empty_label.grid(row=5, column=2, sticky="nsew")
        self.button_label4 = Label(self.frame, width=25, height=5, text="By: Nohad Zamel", anchor=S)
        self.button_label4.grid(row=6, column=2, sticky="nsew")

        self.button1 = Button(self.button_label1, text="Play Game", width=25, height=5, command=self.open_game_window)
        self.button1.grid()

        self.button2 = Button(self.button_label2, text="Options", width=25, height=5, command=self.open_options_window)
        self.button2.grid()

        self.button3 = Button(self.button_label3, text="High Scores", width=25, height=5, command=self.open_high_scores_window)
        self.button3.grid()

    def open_game_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Game(self.newwindow)

    def open_options_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Options(self.newwindow)

    def open_high_scores_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = HighScore(self.newwindow)


def main():
    root = Tk()
    root.title("Quiz Game")
    app = MainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
