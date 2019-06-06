from tkinter import *
from game import *
from highscoreentries import *


class GameScore:

    def __init__(self, master, Game):
        self.master = master
        self.master.geometry("400x200")
        self.master.resizable(width=False, height=False)
        self.game = Game

        self.frame = Frame(self.master, width=400, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.frame.pack(fill="both", expand=True)

        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=2)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)
        self.frame.rowconfigure(7, weight=1)

        self.name_label = Label(self.frame, text="Name: ", )
        self.name_label.grid(column=0, row=2, sticky="NSWE")

        self.submit = Button(self.frame, text="Submit", command=self.get_name)
        self.submit.grid(column=2, row=2)

        self.empty_label1 = Label(self.frame)
        self.empty_label1.grid(column=0, row=3, columnspan=3, sticky="NSWE")

        self.current_top_score = Label(self.frame, text=("Top score: " + score_dict["First"][0] + " with " + str(score_dict["First"][1]) + " points!"), anchor=W)
        self.current_top_score.grid(column=0, row=4, rowspan=2, columnspan=3, sticky="NSWE")

        self.minimum_score = Label(self.frame, text=("Lowest score: " + score_dict["Twentieth"][0] + " with " + str(score_dict["Twentieth"][1]) + " points!"), anchor=W)
        self.minimum_score.grid(column=0, row=6, rowspan=2, columnspan=3, sticky="NSWE")

        self.name_title = Label(self.frame, text="Your Score: " + str(Game.NUM_CORRECT), font="Times 20")
        self.name_title.grid(column=0, row=0, rowspan=2, columnspan=2, sticky="NSWE")

        self.entry1 = Entry(self.frame)
        self.entry1.grid(column=1, row=2)

    def get_name(self):
        name_of_user = self.entry1.get()
        print(name_of_user)
        return name_of_user


infile = open("currenthighscores", "rb")
score_dict = pickle.load(infile)
infile.close()

# def determine_placement():
#     f = open("currenthighscores", "wb")
#     score_dict_2 = pickle.load(f)
#     if score_dict_2["Twentieth"][1] >= Game.NUM_CORRECT:
#         pass
#     else:
#         for x in score_dict_2:
#             if x[1] < Game.NUM_CORRECT:




