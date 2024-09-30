import socket
import sys
import os
from tkinter import ttk, END, Text, Scrollbar
from tkinter import BOTH, LEFT
from tkinter import *
from  tkinter.ttk import Button, Label
import serial
import time
import random
import csv
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import my_speech_recognition

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
file = open("demo.txt", "r")
theme_color=file.read()
if theme_color in ["blue" , "green", "dark-blue"]:
    customtkinter.set_default_color_theme(theme_color)  # Themes: "blue" (standard), "green", "dark-blue", "sweetkind"
speach=""

PATH = os.path.dirname(os.path.realpath(__file__))
class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 660
    

    def __init__(self,*args, **kw):
        super().__init__(*args, **kw)

        self.title("New_Gui.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.com = None
        image = Image.open(PATH + "/test_images/bg_gradient.jpg")
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        global speach


        
        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.frame_left = customtkinter.CTkFrame(master=self,width=180)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        IMAGE_WIDTH = 140
        IMAGE_HEIGHT = 140
        IMAGE_PATH = r'E:\python\test_images\Goofy_Chacha_Avatar-fotor-20230803171133.png'
        your_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
        self.label_0 = customtkinter.CTkLabel(master=self.frame_left, image=your_image, text='')
        self.label_0.grid(row=1, column=0, pady=10, padx=10)


        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Goofy Chacha",
                                              font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=2, column=0, pady=10, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.frame_left,width=120)
        
        self.entry.insert(0, "com4")
        
        self.entry.grid(row=3, column=0, pady=10, padx=20,sticky="n")
        

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="select",
                                                command=lambda: self.update_value(self.entry.get()))
        self.button_1.grid(row=4, column=0, pady=10, padx=20,sticky="n")

        self.radio_var_color = tkinter.IntVar(value=0)

        self.radio_blue = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           text="blue",
                                                           variable=self.radio_var_color,
                                                           font=("Roboto Medium", 13),
                                                           command=lambda:self.change_color_mode('blue'),
                                                           value=0)
        self.radio_blue.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.radio_green = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           text="green",
                                                           variable=self.radio_var_color,
                                                           font=("Roboto Medium", 13),
                                                           command=lambda:self.change_color_mode('green'),
                                                           value=1)
        self.radio_green.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(11, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(0, weight=3)
        self.frame_right.columnconfigure(1, weight=3)
        self.frame_right.columnconfigure(2, weight=3)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=1, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Turn On or Off",
                                                   height=50,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   font=("Roboto Medium", 25),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        img=customtkinter.CTkImage(Image.open(r"E:\python\test_images\mic.png"))
        
        self.button_3 = customtkinter.CTkButton(master=self.frame_info,
                                                image=img,
                                                height=50,
                                                width=40,
                                                text="",
                                                border_width=0,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=lambda:[self.speach(),self.send_value(speach.encode()),self.entry2.delete(0, END)])
        self.button_3.grid(row=0, column=2, padx=15, pady=15, sticky="nwe")

        # ============ frame_right ============
        sock = None
        
        self.radio_var1 = tkinter.IntVar(value=0)
        self.radio_var2 = tkinter.IntVar(value=1)
        self.radio_var3 = tkinter.IntVar(value=2)
        self.radio_var4 = tkinter.IntVar(value=3)
        self.radio_var5 = tkinter.IntVar(value=4)
        self.radio_var6 = tkinter.IntVar(value=5)
        self.radio_var7 = tkinter.IntVar(value=6)
        self.radio_var8 = tkinter.IntVar(value=7)
        self.radio_var9 = tkinter.IntVar(value=8)
        self.radio_var10 = tkinter.IntVar(value=9)

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           text="1.Light On",
                                                           variable=self.radio_var1,
                                                           font=("Roboto Medium", 13),
                                                           command=lambda:self.send_value('11'.encode()),
                                                           value=0)
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           text="1.Light Off",
                                                           variable=self.radio_var1,
                                                           font=("Roboto Medium", 13),
                                                           command=lambda:self.send_value('9'.encode()),
                                                           value=1)
        self.radio_button_2.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Add a Text widget to display received data
        self.received_text_frame = Frame(self.frame_right, bd=1, relief=SUNKEN)
        self.received_text_frame.grid(row=2, column=0, columnspan=2, rowspan=9, pady=10, padx=20, sticky="nsew")
        self.received_text = Text(self.received_text_frame, wrap=WORD)
        self.received_text.grid(row=0, column=0, sticky="nsew")
        self.received_text_scroll = Scrollbar(self.received_text_frame, orient=VERTICAL, command=self.received_text.yview)
        self.received_text_scroll.grid(row=0, column=1, sticky='nsew')
        self.received_text.config(yscrollcommand=self.received_text_scroll.set)
        self.received_text.config(state=DISABLED)

        self.entry2 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=30,
                                            placeholder_text="Message")
        self.entry2.grid(row=12, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Send",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=lambda:[self.send_value((str(self.entry2.get())).encode()),self.entry2.delete(0, END)])
        self.button_2.grid(row=12, column=2, columnspan=1, pady=20, padx=20, sticky="we")


        # set default values
        self.optionmenu_1.set("Dark")
        file = open("demo.txt", "r")
        new_color_mode = file.read()
        if new_color_mode in ["blue", "green", "dark-blue", "sweetkind"]:
            exec('self.radio_'+new_color_mode+'.select()')
        for child in range(1,21):
            a='self.radio_button_'+(str(child))+'.configure(state = DISABLED)'
            exec(a)
        for child in range(2,21,2):
            b='self.radio_button_'+(str(child))+'.select()'
            exec(b)
        self.entry2.configure(state="disabled")
        self.button_2.configure(state="disabled", text="disabled")
    def speach(self):
        global speach
        speach=my_speech_recognition.speech_to_text()
    def update_bluetooth_devices(self):
        #self.devices = bluetooth.discover_devices(duration=20, lookup_names=True)
        self.devices = [["00:21:07:00:06:c0", "hoc"]]
        self.devices = [f"{i[0]},{i[1]}" for i in self.devices]
        if self.listbox is not None:
            self.listbox.delete(0, END)  # clear listbox
            for device in self.devices:  # populate listbox again
                self.listbox.insert(END, device)
    
    def update_value(self,value):
        self.sock = serial.Serial(port=value.upper(), baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, stopbits=1)
        size = 1024
        self.button_1.configure(state="disabled", text="Selected")
        self.entry.configure(state="disabled")
        for child in range(1,21):
            a='self.radio_button_'+(str(child))+'.configure(state="normal")'
            exec(a)
        self.entry2.configure(state="normal")
        self.button_2.configure(state="normal", text="Send")
        

    def send_value(self, value):
        self.sock.write(value)
        received_data = self.sock.readline().decode()
        self.received_text.config(state=NORMAL)
        self.received_text.insert(END, received_data)
        self.received_text.config(state=DISABLED)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_color_mode(self, new_color_mode):
        file = open("demo.txt", "w")
        file.write(new_color_mode)
        file.close()
        self.destroy()
        import new_gui
        
    def on_closing(self, event=0):
        self.destroy()
        

app = App()
app.mainloop()
