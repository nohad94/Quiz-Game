from tkinter import *

APP_NAME = "Quiz Game"


class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.resizable(False, False)

        self.frame = Frame(self.master)
        self.frame.pack_propagate(0)
        self.frame.grid(row=0, columnspan=5)

        self.title = Label(self.frame, width=35, height=5, text="Quiz Game", font="times 19")
        self.title.grid()

        self.button_label1 = Label(self.master, width=100, height=100)
        self.button_label1.grid(row=2, column=2)
        self.button_label2 = Label(self.master, width=100, height=100)
        self.button_label2.grid(row=3, column=2)
        self.button_label3 = Label(self.master, width=25, height=5, borderwidth=2, text="By: Nohad Zamel", anchor=S)
        self.button_label3.grid(row=5, column=2)
        self.button_label4 = Label(self.master, width=100, height=100)
        self.button_label4.grid(row=4, column=2)

        self.button1 = Button(self.button_label1, text="Play Game", width=25, height=5, command=self.open_game_window)
        self.button1.grid()

        self.button2 = Button(self.button_label2, text="Options", width=25, height=5, command=self.open_options_window)
        self.button2.grid()

        self.button3 = Button(self.button_label4, text="High Scores", width=25, height=5, command=self.open_high_scores_window)
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


class Game:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.resizable(False, False)

        self.frame = Frame(self.master)
        self.frame.pack_propagate(0)
        self.frame.grid(row=0, columnspan=5)

        self.title = Label(self.frame, width=35, height=5, text="What is the fifth element in the 4th row of the periodic table?", font="times 19", wraplength=500)
        self.title.grid()

        self.button_label1 = Label(self.master, width=100, height=50, font="times 5")
        self.button_label1.grid(row=3, column=1)
        self.button_label2 = Label(self.master, width=100, height=50, font="times 5")
        self.button_label2.grid(row=3, column=3)
        self.button_label3 = Label(self.master, width=100, height=50, font="times 5")
        self.button_label3.grid(row=5, column=1)
        self.button_label4 = Label(self.master, width=100, height=50, font="times 5")
        self.button_label4.grid(row=5, column=3)

        self.button1 = Button(self.button_label1, text="A", width=20, height=4)
        self.button1.grid()

        self.button2 = Button(self.button_label2, text="B", width=20, height=4)
        self.button2.grid()

        self.button3 = Button(self.button_label3, text="C", width=20, height=4)
        self.button3.grid()

        self.button4 = Button(self.button_label4, text="D", width=20, height=4)
        self.button4.grid()



class Options:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.resizable(False, False)


class HighScore:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.resizable(False, False)


def main():
    root = Tk()
    root.title("Quiz Game")
    app = MainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
