from MainMenu import *
from Question import *
import random


class Game:
    def __init__(self, master):
        self.user_answer = ""
        self.question_number = 0
        self.number_of_correct_answers = 0
        self.question_list = list(set([random.choice(list_of_questions) for x in range(10)]))

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

        self.question = random.choice(self.question_list)
        self.title = Label(self.frame, width=35, height=10, text=self.question, font="times 19", wraplength=350)
        self.title.grid(row=0, column=0, columnspan=5, rowspan=2, sticky="nsew")

        self.button_label1 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label1.grid(row=2, column=1)
        self.button_label2 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label2.grid(row=2, column=3)
        self.button_label3 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label3.grid(row=4, column=1)
        self.button_label4 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label4.grid(row=4, column=3)

        self.possibilities = dic_possibilities[self.question]
        self.possibility1 = self.possibilities[0]
        self.possibility2 = self.possibilities[1]
        self.possibility3 = self.possibilities[2]
        self.possibility4 = self.possibilities[3]

        self.button1 = Button(self.button_label1, text=self.possibility1, width=20, height=4, command=self.return_text_1)
        self.button1.grid()

        self.button2 = Button(self.button_label2, text=self.possibility2, width=20, height=4, command=self.return_text_2)
        self.button2.grid()

        self.button3 = Button(self.button_label3, text=self.possibility3, width=20, height=4, command=self.return_text_3)
        self.button3.grid()

        self.button4 = Button(self.button_label4, text=self.possibility4, width=20, height=4, command=self.return_text_4)
        self.button4.grid()

    def return_text_1(self):
        self.user_answer = self.button1["text"]
        if self.user_answer == dic_answers[self.title["text"]]:
            self.number_of_correct_answers += 1
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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
        self.user_answer = self.button2["text"]
        if self.user_answer == dic_answers[self.title["text"]]:
            self.number_of_correct_answers += 1
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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
        self.user_answer = self.button2["text"]
        if self.user_answer == dic_answers[self.title["text"]]:
            self.number_of_correct_answers += 1
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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
        self.user_answer = self.button2["text"]
        if self.user_answer == dic_answers[self.title["text"]]:
            self.number_of_correct_answers += 1
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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
            print(self.question_list)
            self.question_list = self.question_list[1:]
            print(self.question_list)
            #  reseting the text of button and question labels
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

    def new_question(self):
        while self.question_number < 16:
            self.question_number += 1
            if self.question_number == 16:
                break
            if self.user_answer == dic_answers[self.title["text"]]:
                self.number_of_correct_answers += 1
                self.question_list = self.question_list[1:]
            else:
                self.question_list = self.question_list[1:]

