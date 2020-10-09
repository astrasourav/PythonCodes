import tkinter as tk

class FeeReport:
    def fee_report(self):
        root = tk.Tk()

        root.title('Fee Report')

        root.geometry("655x333")
        root.minsize(655, 333)
        root.maxsize(655, 333)

        # Creating Frame and Label for heading
        frame_1 = tk.Frame(root, borderwidth=10)
        frame_1.pack(pady=10)

        heading = tk.Label(frame_1, text='Fee Report', font="consolas 20 bold")
        heading.pack()

        # Creating Frame and Label for button 1
        frame_2 = tk.Frame(root, borderwidth=10)
        frame_2.pack(pady=15)

        button_1 = tk.Button(frame_2, text='Admin Login', width=15, height=2, command=root.destroy)
        button_1.pack()

        # Creating Frame and Label for Button 2
        frame_3 = tk.Frame(root, borderwidth=10)
        frame_3.pack(pady=10)

        button_2 = tk.Button(frame_3, text='Accountant Login', width=15, height=2, command=root.destroy)
        button_2.pack()

        root.mainloop()
