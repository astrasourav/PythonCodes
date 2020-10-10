import tkinter as tk
from tkinter import *

class Fee_Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Fee Report")
        self.root.geometry("630x300")

        # Creating a Frame for the Label of our GUI
        frame1 = tk.Frame(self.root)
        frame1.grid()

        self.label = tk.Label(frame1, text="Fee Report", font="consolas 20 bold", borderwidth=3)
        self.label.grid(padx=250)

        # Creating a Frame and Button for Admin Login
        frame2 = tk.Frame(self.root)
        frame2.grid()

        self.butt_1 = tk.Button(frame2, text="Admin Login", borderwidth=3)
        self.butt_1.grid(pady=60)

        # Creating a Frame and Button for Accountant Login
        frame3 = tk.Frame(self.root)
        frame3.grid()

        self.butt_3 = tk.Button(frame3, text='Accountant Login', borderwidth=3)
        self.butt_3.grid()
