from mainmenu import *
import tkinter
import pickle


class HighScore:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x700")

        self.frame = Frame(self.master, width=500, height=500, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.frame.pack(fill="both", expand=True)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)
        self.frame.rowconfigure(7, weight=1)
        self.frame.rowconfigure(8, weight=1)
        self.frame.rowconfigure(9, weight=1)
        self.frame.rowconfigure(10, weight=1)
        self.frame.rowconfigure(11, weight=1)
        self.frame.rowconfigure(12, weight=1)

        self.frame1 = Frame(self.frame, width=500)
        self.frame1.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="NSWE")

        self.frame1_label = Label(self.frame1, text="High Scores")
        self.frame1_label.grid(sticky="NSWE")

        self.frame1.rowconfigure(0, weight=1)
        self.frame1.columnconfigure(0, weight=1)

        self.frame2 = Frame(self.frame, width=500)
        self.frame2.grid(row=2, column=0, columnspan=3, sticky="NSWE")

        self.frame2_button1 = Button(self.frame2, text="Game1")
        self.frame2_button1.grid(row=2, column=0, sticky="NSWE")
        self.frame2_button2 = Button(self.frame2, text="Game2")
        self.frame2_button2.grid(row=2, column=1, sticky="NSWE")
        self.frame2_button3 = Button(self.frame2, text="Game3")
        self.frame2_button3.grid(row=2, column=2, sticky="NSWE")

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        self.frame2.columnconfigure(2, weight=1)

        self.frame3 = Frame(self.frame, width=500)
        self.frame3.grid(row=3, rowspan=10, column=0, columnspan=3, sticky="NSWE")

        self.frame3_label1 = Label(self.frame3, text=score_dict[0][0] + ", " + str(score_dict[0][1]), relief="raised")
        self.frame3_label1.grid(row=3, column=0, sticky="NSWE")
        self.frame3_label2 = Label(self.frame3, text=score_dict[1][0] + ", " + str(score_dict[1][1]), relief="raised")
        self.frame3_label2.grid(row=4, column=0, sticky="NSWE")
        self.frame3_label3 = Label(self.frame3, text=score_dict[2][0] + ", " + str(score_dict[2][1]), relief="raised")
        self.frame3_label3.grid(row=5, column=0, sticky="NSWE")
        self.frame3_label4 = Label(self.frame3, text=score_dict[3][0] + ", " + str(score_dict[3][1]), relief="raised")
        self.frame3_label4.grid(row=6, column=0, sticky="NSWE")
        self.frame3_label5 = Label(self.frame3, text=score_dict[4][0] + ", " + str(score_dict[4][1]), relief="raised")
        self.frame3_label5.grid(row=7, column=0, sticky="NSWE")
        self.frame3_label6 = Label(self.frame3, text=score_dict[5][0] + ", " + str(score_dict[5][1]), relief="raised")
        self.frame3_label6.grid(row=8, column=0, sticky="NSWE")
        self.frame3_label7 = Label(self.frame3, text=score_dict[6][0] + ", " + str(score_dict[6][1]), relief="raised")
        self.frame3_label7.grid(row=9, column=0, sticky="NSWE")
        self.frame3_label8 = Label(self.frame3, text=score_dict[7][0] + ", " + str(score_dict[7][1]), relief="raised")
        self.frame3_label8.grid(row=10, column=0, sticky="NSWE")
        self.frame3_label9 = Label(self.frame3, text=score_dict[8][0] + ", " + str(score_dict[8][1]), relief="raised")
        self.frame3_label9.grid(row=11, column=0, sticky="NSWE")
        self.frame3_label10 = Label(self.frame3, text=score_dict[9][0] + ", " + str(score_dict[9][1]), relief="raised")
        self.frame3_label10.grid(row=12, column=0, sticky="NSWE")

        self.frame3_label11 = Label(self.frame3, text=score_dict[10][0] + ", " + str(score_dict[10][1]), relief="raised")
        self.frame3_label11.grid(row=3, column=2, sticky="NSWE")
        self.frame3_label12 = Label(self.frame3, text=score_dict[11][0] + ", " + str(score_dict[11][1]), relief="raised")
        self.frame3_label12.grid(row=4, column=2, sticky="NSWE")
        self.frame3_label13 = Label(self.frame3, text=score_dict[12][0] + ", " + str(score_dict[12][1]), relief="raised")
        self.frame3_label13.grid(row=5, column=2, sticky="NSWE")
        self.frame3_label14 = Label(self.frame3, text=score_dict[13][0] + ", " + str(score_dict[13][1]), relief="raised")
        self.frame3_label14.grid(row=6, column=2, sticky="NSWE")
        self.frame3_label15 = Label(self.frame3, text=score_dict[14][0] + ", " + str(score_dict[14][1]), relief="raised")
        self.frame3_label15.grid(row=7, column=2, sticky="NSWE")
        self.frame3_label16 = Label(self.frame3, text=score_dict[15][0] + ", " + str(score_dict[15][1]), relief="raised")
        self.frame3_label16.grid(row=8, column=2, sticky="NSWE")
        self.frame3_label17 = Label(self.frame3, text=score_dict[16][0] + ", " + str(score_dict[16][1]), relief="raised")
        self.frame3_label17.grid(row=9, column=2, sticky="NSWE")
        self.frame3_label18 = Label(self.frame3, text=score_dict[17][0] + ", " + str(score_dict[17][1]), relief="raised")
        self.frame3_label18.grid(row=10, column=2, sticky="NSWE")
        self.frame3_label19 = Label(self.frame3, text=score_dict[18][0] + ", " + str(score_dict[18][1]), relief="raised")
        self.frame3_label19.grid(row=11, column=2, sticky="NSWE")
        self.frame3_label20 = Label(self.frame3, text=score_dict[19][0] + ", " + str(score_dict[19][1]), relief="raised")
        self.frame3_label20.grid(row=12, column=2, sticky="NSWE")

        self.frame3.columnconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=0)
        self.frame3.columnconfigure(2, weight=1)
        self.frame3.rowconfigure(3, weight=1)
        self.frame3.rowconfigure(4, weight=1)
        self.frame3.rowconfigure(5, weight=1)
        self.frame3.rowconfigure(6, weight=1)
        self.frame3.rowconfigure(7, weight=1)
        self.frame3.rowconfigure(8, weight=1)
        self.frame3.rowconfigure(9, weight=1)
        self.frame3.rowconfigure(10, weight=1)
        self.frame3.rowconfigure(11, weight=1)
        self.frame3.rowconfigure(12, weight=1)


infile = open("currenthighscores.txt", "rb")
score_dict = pickle.load(infile)
infile.close()

