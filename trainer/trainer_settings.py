from tkinter import *
import tkinter
from PIL import ImageTk, Image

closePic = Image.open('assets/close.png')
closePic = closePic.resize((35, 35), Image.Resampling.LANCZOS)

def launch():
    win = Toplevel()
    win.configure(width=600, height=800)
    win.configure(bg='#FBF6F6')
    win.resizable(False, False)
    #win.overrideredirect(1)
    #win.eval('tk::PlaceWindow . center')
    #position screen
    screen_width = win.winfo_screenwidth()  # Width of the screen
    screen_height = win.winfo_screenheight()  # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (800 / 2)
    w=600
    h=800
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Settings Label
    Label(win, text='SETTINGS', bg='#C2CCF2', font='none 25', width=29, height=3).place(x=0, y=0)

    #Close button
    def close():
        win.destroy()
        # closePic = Image.open('assets/close.png')
        # closePic = closePic.resize((35, 35), Image.Resampling.LANCZOS)
        test = ImageTk.PhotoImage(closePic)
        Button(win, text='CLOSE', image=test, bg='#FFF3C7', command=close).place(x=560, y=120)

    #restart
    Button(win, text='Change Password', width=30, height=3, font='none 12', bg='#FFF3C7', command='').place(x=140, y=200)

    #rest time
    Button(win, text='Give your Feedback', width=30, height=3, font='none 12', bg='#FFF3C7', command='').place(x=140, y=350)

    # #share progress
    # Button(win, text='Give your Feedback', width=30, height=3, font='none 12', bg='#FFF3C7', command='').place(x=140, y=500)



    win.mainloop()