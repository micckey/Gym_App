# from tkinter import *
#
#
# class GUI(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("744x377")
#
#     def status(self):
#         self.var = StringVar()
#         self.var.set("Ready")
#         self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
#         self.statusbar.pack(side=BOTTOM, fill=X)
#
#     def click(self):
#         print("Button clicked")
#
#     def createbutton(self, inptext):
#         Button(text=inptext, command=self.click).pack()
#
#
# if __name__ == '__main__':
#     window = GUI()
#     window.status()
#     window.createbutton("Click me")
#     window.mainloop()

import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()