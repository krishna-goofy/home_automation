import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
import encription
import csv

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


class App2(customtkinter.CTk):

    APP_NAME = "CustomTkinter example_background_image.py"
    WIDTH = 780
    HEIGHT = 660

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App2.APP_NAME)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        #load image with PIL and convert to PhotoImage
        image = Image.open(PATH + "/test_images/bg_gradient.jpg")
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.frame = customtkinter.CTkFrame(master=self,
                                            width=300,
                                            height=App2.HEIGHT,
                                            corner_radius=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label_1 = customtkinter.CTkLabel(master=self.frame, width=200, height=60,
                                              fg_color=("gray70", "gray25"), text="CustomTkinter\ninterface example")
        self.label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame, corner_radius=6, width=200, placeholder_text="username")
        self.entry_1.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame, corner_radius=6, width=200, show="*", placeholder_text="password")
        self.entry_2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.button_2 = customtkinter.CTkButton(master=self.frame, text="Login",
                                                corner_radius=6, command=self.button_event, width=200)
        self.button_2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def button_event(self):
        username=encription.encrip(self.entry_1.get())
        password=encription.encrip(self.entry_2.get())
        full=[username+"\n",password+"\n"]
        with open('Passwords.csv') as csvfile:
            file = csv.reader(csvfile)
            for data in file:
                if full == data:
                    self.app2()
                    
                    
                else:
                    self.label_2 = customtkinter.CTkLabel(master=self.frame, width=200, height=60,
                                                          fg_color=("gray70", "gray25"), text="Incorrect")
                    self.label_2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
                    
    def app2(self):
        self.destroy()
        import new_gui
    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app2 = App2()
    app2.start()
