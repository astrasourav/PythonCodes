import tkinter as tk


def aaa(admin_GUI):
    if admin_GUI.userentry == 'admin' and admin_GUI.passentry == '1234':
        print("Welcome")
    else:
        print("Invalid user")


class admin_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Admin Login')
        self.root.geometry('630x300')

        self.heading = tk.Label(root, text='Admin Login', font='consolas 20 bold')
        self.heading.place(relx=0.5, rely=0.09, anchor='center')

        self.user = tk.Label(root, text='Name:')
        self.password = tk.Label(root, text='Password:')
        self.user.grid(row=0, column=0, padx=100, pady=80)
        self.password.grid(row=1, column=0, pady=2)

        self.userval = tk.StringVar()
        self.passval = tk.StringVar()

        self.userentry = tk.Entry(root, textvariable=self.userval)
        self.passentry = tk.Entry(root, textvariable=self.passval, show='*')
        self.userentry.grid(row=0, column=1, pady=80)
        self.passentry.grid(row=1, column=1, pady=2)

        self.submit = tk.Button(root, text='Submit', command=aaa)
        self.submit.grid(row=2, column=1, pady=40)
