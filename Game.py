from MainMenu import *
from Question import *
import random


class Game:
    NUM = 10
    NUM_CORRECT = 0

    def __init__(self, master):
        self.user_answer = ""
        self.question_number = 0
        self.question_list = Game.create_question_list(self)

        self.master = master
        self.master.geometry("500x700")

        self.frame = Frame(self.master, width=500, height=500, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.frame.pack(fill="both", expand=True)

        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=0)
        self.frame.rowconfigure(5, weight=2)
        self.frame.columnconfigure(0, weight=2)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(4, weight=2)

        self.question = self.question_list[0]
        self.title = Label(self.frame, width=35, height=10, text="Start Game", font="times 19", wraplength=350)
        self.title.grid(row=0, column=0, columnspan=5, rowspan=2, sticky="nsew")

        self.button_label1 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label1.grid(row=2, column=1)
        self.button_label2 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label2.grid(row=2, column=3)
        self.button_label3 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label3.grid(row=4, column=1)
        self.button_label4 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label4.grid(row=4, column=3)

        self.score = Label(self.frame, text=(str(0) + " out of " + str(Game.NUM)))
        self.score.grid(row=6, column=0, columnspan=5, rowspan=1)

        self.possibilities = dic_possibilities[self.question]
        self.possibility1 = self.possibilities[0]
        self.possibility2 = self.possibilities[1]
        self.possibility3 = self.possibilities[2]
        self.possibility4 = self.possibilities[3]

        self.button1 = Button(self.button_label1, text="Yes", width=20, height=4, command=self.return_text_1)
        self.button1.grid()

        self.button2 = Button(self.button_label2, text="No", width=20, height=4, command=self.return_text_2)
        self.button2.grid()

        self.button3 = Button(self.button_label3, text="", width=20, height=4, command=self.return_text_3)
        self.button3.grid()

        self.button4 = Button(self.button_label4, text="", width=20, height=4, command=self.return_text_4)
        self.button4.grid()

    def create_question_list(self):
        question_list = []
        while len(question_list) <= Game.NUM:
            if len(question_list) == Game.NUM:
                return question_list
            question = random.choice(list_of_questions)
            if question in question_list:
                pass
            else:
                question_list.append(question)

    def return_text_1(self):
        print(self.question_list)
        self.user_answer = self.button1["text"]
        if self.user_answer == "Yes":
            self.title["text"] = self.question_list[0]
            self.possibilities = dic_possibilities[self.title["text"]]
            self.possibility1 = self.possibilities[0]
            self.button1["text"] = self.possibility1
            self.possibility2 = self.possibilities[1]
            self.button2["text"] = self.possibility2
            self.possibility3 = self.possibilities[2]
            self.button3["text"] = self.possibility3
            self.possibility4 = self.possibilities[3]
            self.button4["text"] = self.possibility4
        else:
            if self.user_answer == dic_answers[self.title["text"]]:
                Game.NUM_CORRECT += 1
                self.score["text"] = (str(Game.NUM_CORRECT) + " out of " + str(Game.NUM))
            else:
                pass
            self.question_list = self.question_list[1:]
            Game.check_question_list(self)
            self.title["text"] = self.question_list[0]
            self.possibilities = dic_possibilities[self.title["text"]]
            self.possibility1 = self.possibilities[0]
            self.button1["text"] = self.possibility1
            self.possibility2 = self.possibilities[1]
            self.button2["text"] = self.possibility2
            self.possibility3 = self.possibilities[2]
            self.button3["text"] = self.possibility3
            self.possibility4 = self.possibilities[3]
            self.button4["text"] = self.possibility4

    def return_text_2(self):
        print(self.question_list)
        self.user_answer = self.button2["text"]
        if self.user_answer == "No":
            self.master.destroy()
        else:
            if self.user_answer == dic_answers[self.title["text"]]:
                Game.NUM_CORRECT += 1
                self.score["text"] = (str(Game.NUM_CORRECT) + " out of " + str(Game.NUM))
            else:
                pass
            self.question_list = self.question_list[1:]
            Game.check_question_list(self)
            self.title["text"] = self.question_list[0]
            self.possibilities = dic_possibilities[self.title["text"]]
            self.possibility1 = self.possibilities[0]
            self.button1["text"] = self.possibility1
            self.possibility2 = self.possibilities[1]
            self.button2["text"] = self.possibility2
            self.possibility3 = self.possibilities[2]
            self.button3["text"] = self.possibility3
            self.possibility4 = self.possibilities[3]
            self.button4["text"] = self.possibility4

    def return_text_3(self):
        print(self.question_list)
        self.user_answer = self.button3["text"]
        if self.user_answer == dic_answers[self.title["text"]]:
            Game.NUM_CORRECT += 1
            self.score["text"] = (str(Game.NUM_CORRECT) + " out of " + str(Game.NUM))
        else:
            pass
        self.question_list = self.question_list[1:]
        Game.check_question_list(self)
        self.title["text"] = self.question_list[0]
        self.possibilities = dic_possibilities[self.title["text"]]
        self.possibility1 = self.possibilities[0]
        self.button1["text"] = self.possibility1
        self.possibility2 = self.possibilities[1]
        self.button2["text"] = self.possibility2
        self.possibility3 = self.possibilities[2]
        self.button3["text"] = self.possibility3
        self.possibility4 = self.possibilities[3]
        self.button4["text"] = self.possibility4

    def return_text_4(self):
        print(self.question_list)
        self.user_answer = self.button4["text"]
        if self.user_answer == dic_answers[self.title["text"]]:
            Game.NUM_CORRECT += 1
            self.score["text"] = (str(Game.NUM_CORRECT) + " out of " + str(Game.NUM))
        else:
            pass
        self.question_list = self.question_list[1:]
        Game.check_question_list(self)
        self.title["text"] = self.question_list[0]
        self.possibilities = dic_possibilities[self.title["text"]]
        self.possibility1 = self.possibilities[0]
        self.button1["text"] = self.possibility1
        self.possibility2 = self.possibilities[1]
        self.button2["text"] = self.possibility2
        self.possibility3 = self.possibilities[2]
        self.button3["text"] = self.possibility3
        self.possibility4 = self.possibilities[3]
        self.button4["text"] = self.possibility4

    def check_question_list(self):
        if len(self.question_list) == 0:
            self.master.destroy()

