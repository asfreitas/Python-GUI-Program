#!/usr/bin/python3

import tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        w = tk.Label(self.master, text="hello")
        w.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
