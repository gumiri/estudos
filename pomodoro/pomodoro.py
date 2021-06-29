#!/usr/bin/python3

from tkinter import *
from playsound import playsound
from math import floor

class Interface(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.makeGUI()
        self.sec = 1000
        self.times = 2
        self.workTime = 1200
        self.showInsert = True
        self.stop = True
        self.reset = True
        self.counter = 0
        self.text = StringVar()
        self.text.set(self.toText())
        self.counterLabel(self.text)
        self.insertText()
        self.insertButton()
        self.startButton()
        self.stopButton()

    def toText(self):
        ds = 0
        s = self.counter
        dm = 0
        m = 0
        while(s >= 600):
            dm += 1
            s -= 600
        while(s >= 60):
            m += 1
            s -= 60
        while(s >= 10):
            ds += 1
            s -= 10
        text = ("{}{}.{}{}".format(dm, m, ds, s))
        return text


    def counterLabel(self, text):
        self.text_counter = Label(self.master, textvariable=text)
        self.text_counter["font"] = ("Verdana", "16")
        self.text_counter.place(relx = 0.5, rely = 0.5, y = -15, x = 0, anchor = CENTER)

        

    def makeGUI(self):
        self.master.title("Pomodoro")
        self.master.geometry("250x120")
        self.pack()
        

    def startButton(self):
        start = Button(self.master)
        start["text"] = "start"
        start["font"] = ("Verdana", "14")
        start["width"] = 5
        start.place(relx = 0.5, rely = 0.5, y = 20, x = -50, anchor = CENTER)
        start["command"] = self.start

    def stopButton(self):
        stop = Button(self.master)
        stop["text"] = "stop"
        stop["font"] = ("Verdana", "14")
        stop["width"] = 5
        stop.place(relx = 0.5, rely = 0.5, y = 20, x = 50, anchor = CENTER)
        stop["command"] = self.restart

    def insertText(self):
        self.txt = Text(self.master)
        self.txt["height"] = 1
        self.txt["width"] = 20
        self.txt.place(relx = 0.5, rely = 0.5, y = -40, x = -25, anchor = CENTER)

    def insertButton(self):
        self.insertB = Button(self.master)
        self.insertB["text"] = "put"
        self.insertB["font"] = ("Verdana", "10")
        self.insertB["width"] = 4
        self.insertB["command"] = self.insert
        self.insertB.place(relx = 0.5, rely = 0.5, y = -40, x = 70, anchor = CENTER)

    def insert(self):
        if(self.txt.get("1.0", 'end-1c').isnumeric()):
            self.workTime = int(self.txt.get("1.0",END))*60

        self.txt.place_forget()
        self.insertB.place_forget()

        


    def stopCounter(self):
        self.stop = True
        self.counter = 0
        self.text.set(self.toText())


    def start(self):
        self.stop = False
        self.reset = False
        self.work()


    def restart(self):
        self.stopCounter()
        self.reset = True


    def work(self):
        if (self.reset == False):
            if(self.counter <= self.workTime):
                self.count()
                self.after(self.sec, self.work)
            else:
                playsound("Computer_Magic-Microsift-1901299923.wav")
                self.stopCounter()
                self.stop = False
                self.relax()

    def count(self):
        if(self.stop == False):
            self.counter += 1
            self.text.set(self.toText())

    def relax(self):
        if(self.reset == False):
            if(self.times > 0):
                if(self.counter <= floor(self.workTime/4)):
                    self.count()
                    self.after(self.sec, self.relax)
                else:
                    playsound("Computer_Magic-Microsift-1901299923.wav")
                    self.stopCounter()
                    self.stop = False
                    self.times -= 1
                    self.work()
            elif(self.times == 0 and self.counter <= floor(self.workTime/1.33333)):
                self.count()
                self.after(self.sec, self.relax)
            else:
                playsound("Computer_Magic-Microsift-1901299923.wav")
                self.stopCounter()
                self.stop = False
                self.work()
                self.times = 2


def main():
    root = Tk()
    app = Interface(master = root)
    app.mainloop()


if __name__ == "__main__":
    main()
