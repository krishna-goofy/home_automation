import socket
import sys
import tkinter as tk
from tkinter import ttk, END
from tkinter import BOTH, LEFT
from tkinter import *
from  tkinter.ttk import Button, Label
import serial
import time
import random
import csv
import my_speech_recognition
import customtkinter
MEDFONT = ("Verdana", 20)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
            # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.com = None

            # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

            # initializing frames to an empty array
        self.frames = {}

            # iterating through a tuple consisting
            # of the different page layouts
        for F in (SelectComPort, RelayControl):
            frame = F(container, self)

                # initializing frame of that object from
                # startpage, page1, page2 respectively with
                # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SelectComPort)

        # to display the current frame passed as
        # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.update_value()


    # first window frame startpage
class SelectComPort(tk.Frame):
    def update_bluetooth_devices(self):
        #self.devices = bluetooth.discover_devices(duration=20, lookup_names=True)
        self.devices = [["00:21:07:00:06:c0", "hoc"]]
        self.devices = [f"{i[0]},{i[1]}" for i in self.devices]
        if self.listbox is not None:
            self.listbox.delete(0, END)  # clear listbox
            for device in self.devices:  # populate listbox again
                self.listbox.insert(END, device)

    def update_value(self):
        pass

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.devices = None
        self.listbox = None

            #self.update_bluetooth_devices()
            # label of frame Layout 2
        label = ttk.Label(self, text="Enter COM PORT", font=MEDFONT)

            # putting the grid in its place by using
            # grid
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        refresh = Button(self)
        refresh["text"] = "refresh"
        refresh["command"] = self.update_bluetooth_devices
        refresh.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        langs_var = tk.StringVar(value=self.devices)

        textbox = tk.Entry(self)
        textbox.insert(0, "com3")
        textbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        button = tk.Button(self, text="Select")
        button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        button["command"] = lambda: self.click_on_select(textbox.get())

            # handle event

    def click_on_select(self, value):
        self.controller.com = value
        print(self.controller.com)
        self.controller.show_frame(RelayControl)

# second window frame page1
class RelayControl(tk.Frame):
    sock = None
        
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_1 = customtkinter.CTkLabel(self,text="Turn on/off relay",text_font=("Roboto Medium", 20))
        label_1.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.client = None
        '''
        self.Add_Button = Button(self)
        self.Add_Button["text"] = "Add Button"
        self.Add_Button["command"] = lambda: self.Add_Button2(controller)
        self.Add_Button.grid(row=2, column=0, padx=10, pady=10)
        
        self.speek = Button(self)
        self.speek["text"] = "speak"
        self.speek["command"] = lambda:self.send_value((my_speech_recognition.speech_to_text()).encode())
        self.speek.grid(row=2, column=1, padx=10, pady=10)
        
        self.hello_on = Button(self)
        self.hello_on["text"] = 'hello_on'
        self.hello_on["command"] = lambda: self.send_value('0'.encode())
        self.hello_on.grid(row=3, column=0, padx=10, pady=10)
        
        self.hello_off = Button(self)
        self.hello_off["text"] = 'hello_off'
        self.hello_off["command"] = lambda: self.send_value('1'.encode())
        self.hello_off.grid(row=3, column=1, padx=10, pady=10)
        '''
        
        self.Add_Button = customtkinter.CTkButton(self,text="Add Button",command=lambda:self.Add_Button2(controller))
        self.Add_Button.grid(row=2, column=0, padx=10, pady=10)

        self.speak = customtkinter.CTkButton(self,text="speak",command=lambda:self.send_value(my_speech_recognition.speech_to_text().encode()))
        self.speak.grid(row=2, column=1, padx=10, pady=10)
        
        self.hello_on = customtkinter.CTkButton(self,text="hello_on",command=lambda:self.send_value('0'.encode()))
        self.hello_on.grid(row=3, column=0, padx=10, pady=10)
        
        self.hello_off = customtkinter.CTkButton(self,text="hello_off",command=lambda:self.send_value('1'.encode()))
        self.hello_off.grid(row=3, column=1, pady=10, padx=10)

    def Add_Button2(self,controller):
        self.sock.close()
        tk.Tk.destroy(controller)
        import testing2_add
        testing2_add.app_add_data()
            
    def update_value(self):
        self.sock = serial.Serial(port=self.controller.com.upper(), baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, stopbits=1)
        size = 1024

    def send_value(self, value):
        self.sock.write(value)

    def quit(self):
        self.sock.close()
        super().quit()


# Driver Code
app = tkinterApp()
app.mainloop()
