from tkinter import *
from game import *
from highscoreentries import *
import pickle


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

        self.submit = Button(self.frame, text="Submit", command=lambda: self.update_high_scores())
        self.submit.grid(column=2, row=2)

        self.empty_label1 = Label(self.frame)
        self.empty_label1.grid(column=0, row=3, columnspan=3, sticky="NSWE")

        self.current_top_score = Label(self.frame, text=my_list[0][0] + str(my_list[0][1]), anchor=W)
        self.current_top_score.grid(column=0, row=4, rowspan=2, columnspan=3, sticky="NSWE")

        self.minimum_score = Label(self.frame, text=my_list[-1][0] + str(my_list[-1][1]), anchor=W)
        self.minimum_score.grid(column=0, row=6, rowspan=2, columnspan=3, sticky="NSWE")

        self.name_title = Label(self.frame, text="Your Score: " + str(Game.NUM_CORRECT), font="Times 20")
        self.name_title.grid(column=0, row=0, rowspan=2, columnspan=2, sticky="NSWE")

        self.entry1 = Entry(self.frame)
        self.entry1.grid(column=1, row=2)

    def get_name(self):
        name_of_user = self.entry1.get()
        print(name_of_user)
        return name_of_user

    def get_current_high_score(self):
        file1 = open("currenthighscores.txt", "rb")
        current_high_score_list = pickle.load(file1)
        file1.close()
        return current_high_score_list

    def new_score_list(self):
        user_name = self.get_name()
        user_high_score_entry = [str(user_name), self.game.NUM_CORRECT]
        current_scores = self.get_current_high_score()
        current_scores.append(user_high_score_entry)
        print(current_scores)
        final_list = sorted(current_scores, key=lambda x: x[1], reverse=True)
        print(final_list)
        return final_list

    def update_high_scores(self):
        new_list = self.new_score_list()
        f1 = open("currenthighscores.txt", "wb")
        pickle.dump(new_list, f1)
        f1.close()


outfile = open("currenthighscores.txt", "rb")
my_list = pickle.load(outfile)
outfile.close()


