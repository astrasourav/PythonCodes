import tkinter as tk


class AdminLogin:
    def admin_login(self):
        root = tk.Tk()

        root.title('Admin Login')

        root.geometry("655x333")
        root.minsize(655, 333)
        root.maxsize(655, 333)

        heading = tk.Label(root, text='Admin Login', font='consolas 20 bold')
        heading.place(relx=0.5, rely=0.09, anchor='center')

        user = tk.Label(root, text='Name:')
        password = tk.Label(root, text='Password:')
        user.grid(row = 0, column = 0, padx= 100,pady = 80)
        password.grid(row = 1, column = 0, pady = 2)

        userval = tk.StringVar()
        passval = tk.StringVar()

        userentry = tk.Entry(root, textvariable=userval)
        passentry = tk.Entry(root, textvariable=passval, show='*')
        userentry.grid(row=0, column=1, pady=80)
        passentry.grid(row=1, column=1, pady=2)

        submit = tk.Button(root, text='Submit', command=root.destroy)
        submit.grid(row = 2, column=1, pady=40)

        root.mainloop()


obj = AdminLogin().admin_login()