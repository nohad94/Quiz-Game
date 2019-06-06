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

        self.frame3_label1 = Label(self.frame3, text=score_dict["First"][0] + " with " + str(score_dict["First"][1]) + " points!", relief="raised")
        self.frame3_label1.grid(row=3, column=0, sticky="NSWE")
        self.frame3_label2 = Label(self.frame3, text=score_dict["Second"][0] + " with " + str(score_dict["Second"][1]) + " points!", relief="raised")
        self.frame3_label2.grid(row=4, column=0, sticky="NSWE")
        self.frame3_label3 = Label(self.frame3, text=score_dict["Third"][0] + " with " + str(score_dict["Third"][1]) + " points!", relief="raised")
        self.frame3_label3.grid(row=5, column=0, sticky="NSWE")
        self.frame3_label4 = Label(self.frame3, text=score_dict["Fourth"][0] + " with " + str(score_dict["Fourth"][1]) + " points!", relief="raised")
        self.frame3_label4.grid(row=6, column=0, sticky="NSWE")
        self.frame3_label5 = Label(self.frame3, text=score_dict["Fifth"][0] + " with " + str(score_dict["Fifth"][1]) + " points!", relief="raised")
        self.frame3_label5.grid(row=7, column=0, sticky="NSWE")
        self.frame3_label6 = Label(self.frame3, text=score_dict["Sixth"][0] + " with " + str(score_dict["Sixth"][1]) + " points!", relief="raised")
        self.frame3_label6.grid(row=8, column=0, sticky="NSWE")
        self.frame3_label7 = Label(self.frame3, text=score_dict["Seventh"][0] + " with " + str(score_dict["Seventh"][1]) + " points!", relief="raised")
        self.frame3_label7.grid(row=9, column=0, sticky="NSWE")
        self.frame3_label8 = Label(self.frame3, text=score_dict["Eighth"][0] + " with " + str(score_dict["Eighth"][1]) + " points!", relief="raised")
        self.frame3_label8.grid(row=10, column=0, sticky="NSWE")
        self.frame3_label9 = Label(self.frame3, text=score_dict["Ninth"][0] + " with " + str(score_dict["Ninth"][1]) + " points!", relief="raised")
        self.frame3_label9.grid(row=11, column=0, sticky="NSWE")
        self.frame3_label10 = Label(self.frame3, text=score_dict["Tenth"][0] + " with " + str(score_dict["Tenth"][1]) + " points!", relief="raised")
        self.frame3_label10.grid(row=12, column=0, sticky="NSWE")

        self.frame3_label11 = Label(self.frame3, text=score_dict["Eleventh"][0] + " with " + str(score_dict["Eleventh"][1]) + " points!", relief="raised")
        self.frame3_label11.grid(row=3, column=2, sticky="NSWE")
        self.frame3_label12 = Label(self.frame3, text=score_dict["Twelfth"][0] + " with " + str(score_dict["Twelfth"][1]) + " points!", relief="raised")
        self.frame3_label12.grid(row=4, column=2, sticky="NSWE")
        self.frame3_label13 = Label(self.frame3, text=score_dict["Thirteenth"][0] + " with " + str(score_dict["Thirteenth"][1]) + " points!", relief="raised")
        self.frame3_label13.grid(row=5, column=2, sticky="NSWE")
        self.frame3_label14 = Label(self.frame3, text=score_dict["Fourteenth"][0] + " with " + str(score_dict["Fourteenth"][1]) + " points!", relief="raised")
        self.frame3_label14.grid(row=6, column=2, sticky="NSWE")
        self.frame3_label15 = Label(self.frame3, text=score_dict["Fifteenth"][0] + " with " + str(score_dict["Fifteenth"][1]) + " points!", relief="raised")
        self.frame3_label15.grid(row=7, column=2, sticky="NSWE")
        self.frame3_label16 = Label(self.frame3, text=score_dict["Sixteenth"][0] + " with " + str(score_dict["Sixteenth"][1]) + " points!", relief="raised")
        self.frame3_label16.grid(row=8, column=2, sticky="NSWE")
        self.frame3_label17 = Label(self.frame3, text=score_dict["Seventeenth"][0] + " with " + str(score_dict["Seventeenth"][1]) + " points!", relief="raised")
        self.frame3_label17.grid(row=9, column=2, sticky="NSWE")
        self.frame3_label18 = Label(self.frame3, text=score_dict["Eighteenth"][0] + " with " + str(score_dict["Eighteenth"][1]) + " points!", relief="raised")
        self.frame3_label18.grid(row=10, column=2, sticky="NSWE")
        self.frame3_label19 = Label(self.frame3, text=score_dict["Nineteenth"][0] + " with " + str(score_dict["Nineteenth"][1]) + " points!", relief="raised")
        self.frame3_label19.grid(row=11, column=2, sticky="NSWE")
        self.frame3_label20 = Label(self.frame3, text=score_dict["Twentieth"][0] + " with " + str(score_dict["Twentieth"][1]) + " points!", relief="raised")
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


infile = open("currenthighscores", "rb")
score_dict = pickle.load(infile)
infile.close()

