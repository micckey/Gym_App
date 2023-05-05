from tkinter import *
from PIL import ImageTk, Image
import io
from trainee.workout_screen import workScreen

def launch2(workoutResults):
    win2 = Toplevel()
    win2.configure(width=1040, height=1040)
    win2.configure(bg='#FBF6F6')
    win2.resizable(False, False)
    #win2.overrideredirect(1)
    #win2.eval('tk::PlaceWindow . center')
    # position screen
    screen_width = win2.winfo_screenwidth()  # Width of the screen
    screen_height = win2.winfo_screenheight()  # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (1040 / 2)
    y = (screen_height / 2) - (1040 / 2)
    w = 1040
    h = 1040
    win2.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #heading
    Label(win2, text='WORKOUTS', bg='#C2CCF2', font='none 20', width=61, height=3).place(x=0, y=0)

    #begin button
    Button(win2, text='BEGIN WORKOUT', height=5, pady=5, bg='#FFF3C7', command=lambda: workScreen(workoutResults)).place(x=60, y=0)


    #workouts
    frame = Frame(win2, bg='lightgray')
    frame.place(x=120, y=140)
    frame.pack_propagate(False)

    images = []
    c = 0
    r = 0
    for j in range(9):
        pic = workoutResults[j][0]
        stream = io.BytesIO(pic)
        img = Image.open(stream)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)

        e = Label(frame, image=img)
        e.grid(row=r, column=c, ipady=7, ipadx=7)
        images.append(img)  # garbage collection
        if c == 2:
            r += 1
            c = 0
        else:
            c += 1





    win2.mainloop()
