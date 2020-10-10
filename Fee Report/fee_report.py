import tkinter as tk

class Fee_Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("630x300")

        self.label = tk.Label(root, text="Fee Report")
        self.label.pack()

