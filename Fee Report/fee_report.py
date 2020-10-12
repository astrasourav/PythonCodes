import tkinter as tk
from tkinter import *

from admin_login import admin_GUI


def obj():
    root = tk.Tk()
    app = admin_GUI(root)
    root.mainloop()


class Fee_Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Fee Report")
        self.root.geometry("630x300")

        # Creating a Frame for the Label of our GUI
        space1 = tk.Frame(self.root)
        space1.grid()

        frame1 = tk.Frame(space1, width=630, height=60, padx=20, bd=16)
        frame1.grid(row=0, column=0)

        self.label = tk.Label(frame1, text="Fee Report", font="consolas 20 bold", padx=200)
        self.label.grid(row=0, column=0, sticky=W)

        self.butt_1 = tk.Button(frame1, text="Admin Login", command=obj)
        self.butt_1.grid(pady=50)

        self.butt_3 = tk.Button(frame1, text='Accountant Login', command=root.quit)
        self.butt_3.grid()
