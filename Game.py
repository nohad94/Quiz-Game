from MainMenu import *

class Game:
    def __init__(self, master):
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

        self.title = Label(self.frame, width=35, height=10, text="Question prompt goes here", font="times 19")
        self.title.grid(row=0, column=0, columnspan=5, rowspan=2, sticky="nsew")

        self.button_label1 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label1.grid(row=2, column=1)
        self.button_label2 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label2.grid(row=2, column=3)
        self.button_label3 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label3.grid(row=4, column=1)
        self.button_label4 = Label(self.frame, width=20, height=4, font="times 5")
        self.button_label4.grid(row=4, column=3)

        self.button1 = Button(self.button_label1, text="A", width=20, height=4, command=self.return_text_1)
        self.button1.grid()

        self.button2 = Button(self.button_label2, text="B", width=20, height=4, command=self.return_text_2)
        self.button2.grid()

        self.button3 = Button(self.button_label3, text="C", width=20, height=4, command=self.return_text_3)
        self.button3.grid()

        self.button4 = Button(self.button_label4, text="D", width=20, height=4, command=self.return_text_4)
        self.button4.grid()

    def return_text_1(self):
        print(self.button1["text"])

    def return_text_2(self):
        print(self.button2["text"])

    def return_text_3(self):
        print(self.button3["text"])

    def return_text_4(self):
        print(self.button4["text"])
