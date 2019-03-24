import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonFont = tkFont.Font(family="Arial", size=18)
        self.label = tk.Label(self, text="Noughts and Crosses", font=self.titlefont)
        self.label.grid(row=0, column=1)
        self.goButton = tk.Button(self, text="    Go!    ", command=self.go, bg="green", fg="white")
        self.goButton.grid(row=0, column=0)
        self.buttongrid = tk.Frame(self)
        self.buttongrid.grid(row=1, column=0, sticky="NSEW", columnspan=2)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1, weight=1)

        self.buttons = []
        self.noughtImage = tk.PhotoImage(file="nought.gif")
        self.crossImage = tk.PhotoImage(file="cross.gif")
        self.blank = tk.PhotoImage(file="blank.gif")
        buttonNum = 0
        for rownum in range(3):
            for columnnum in range(3):
                self.buttons.append(tk.Button(self.buttongrid))
                self.buttons[buttonNum].config(width="50", height= "50", image=self.blank, command = lambda x=buttonNum: self.buttonLeftClicked(x))
                self.buttons[buttonNum].grid(row=rownum, column=columnnum, sticky="NSEW")
                buttonNum += 1
        for x in range(3):
            self.buttongrid.rowconfigure(x,weight=1)
            self.buttongrid.columnconfigure(x, weight=1)
        self.go()

    def buttonLeftClicked(self,  pos):
        print("Button", pos, " was left clicked")
        self.buttons[pos]['image']=self.crossImage



    def go(self):
        for button in self.buttons:
            button.config(state="normal", relief="raised", bg="SystemButtonFace", image=self.blank)
        self.gameOn = True


oxo = App()
oxo.geometry("400x400+200+200")
oxo.title("OXO")
oxo.mainloop()