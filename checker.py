import tkinter
from tkinter import ttk
from tkinter import *


def main():
    root = Tk()
    app = window1(root)
class window1:
    def __init__(self,master):
        self.master=master
        self.master.title("hello")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.button1= Button(self.frame, text="Login",width=17,command = lambda:self.new_window(master))
        self.button1.grid(row=3,column=0)
        
        self.button2= Button(self.frame, text="Login",width=17)
        self.button2.grid(row=3,column=1)
        
        self.button2= Button(self.frame, text="Login",width=17)
        self.button2.grid(row=3,column=2)

    def new_window(self,master):
        self.newWindow = Toplevel(self.master)
        self.app = window2(self.newWindow)

class window2:
    def __init__(self,master):
        self.master=master
        self.master.title("hello2")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'cadet blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
main()
