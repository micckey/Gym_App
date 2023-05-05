from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import time
import io
from trainee.wordings_list import descriptionList

count = 0
def workScreen(workoutResults):
    win = Toplevel()
    win.configure(width=1040, height=1100)
    win.configure(bg='#FBF6F6')
    win.resizable(False, False)
    screen_width = win.winfo_screenwidth()  # Width of the screen
    screen_height = win.winfo_screenheight()  # Height of the screen
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (1040 / 2)
    y = (screen_height / 2) - (1040 / 2)
    w = 1040
    h = 1040
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # heading
    Label(win, bg='#C2CCF2', font='none 20', width=61, height=3).place(x=0, y=0)

    # Create Entry Widgets for MM SS
    Label(win, text='TIMER:', bg='#FBF6F6', font='times 20').place(x=50, y=30)
    sec = StringVar()
    Entry(win, textvariable=sec, width=2, font='Helvetica 20').place(x=200, y=30)
    sec.set('00')
    mins = StringVar()
    Entry(win, textvariable=mins, width=2, font='Helvetica 20').place(x=160, y=30)
    mins.set('00')
    # Define the function for the timer
    def countdowntimer():
        times = int(mins.get()) * 60 + int(sec.get())
        while times > -1:
            minute, second = (times // 60, times % 60)
            if minute > 60:
                minute = (minute // 60, minute % 60)
            sec.set(second)
            mins.set(minute)
            # Update the time
            win.update()
            time.sleep(1)
            if times == 0:
                sec.set('00')
                mins.set('00')
            times -= 1


    Button(win, text='START', bd='2', bg='#FFF3C7', font=('Helvetica bold', 10), command=countdowntimer).place(x=162,
                                                                                                               y=70)

    #Select Weights
    def weightFunc(weightOpt):
        if weightType.get() == 'Kettle Bell':
            weightOpt = ['4 kg', '6 kg', '8 kg', '10 kg', '12 kg']
        elif weightType.get() == 'Dumb Bell':
            weightOpt = ['1 kg', '5 kg', '10 kg', '15 kg']
        elif weightType.get() == 'Bar Bell':
            weightOpt = ['5 kg', '15 kg', '20 kg', '30 kg', '40 kg']

        #change weight
        weightDropMenu['menu'].delete(0, 'end')
        for i in weightOpt:
            weightDropMenu['menu'].add_command(label=i, command=tk._setit(weightVal, i))



    Label(win, text='Select Weight:', bg='#FBF6F6', font='times 20').place(x=300, y=30)
    options = ['Kettle Bell', 'Dumb Bell', 'Bar Bell']
    weightType = StringVar(win)
    weightType.set('')
    typeDropMenu = OptionMenu(win, weightType, *options, command=weightFunc)
    typeDropMenu.place(x=470, y=30)

    weightVal = StringVar(win)
    weightVal.set('')
    weightDropMenu = OptionMenu(win, weightVal, None)
    weightDropMenu.place(x=600, y=30)
    

    #Image frame
    frame = Frame(win, bg='lightgray', width=900, height=600)
    frame.place(x=70, y=140)
    frame.pack_propagate(False)
    pic1 = workoutResults[0][0]
    stream1 = io.BytesIO(pic1)
    img1 = Image.open(stream1)
    img1 = img1.resize((900, 600))
    img1 = ImageTk.PhotoImage(img1)

    images = []
    def changeImage():
        global count
        if count < len(workoutResults)-1:
            count += 1
        else:
            count = 0
        pic = workoutResults[count][0]
        stream = io.BytesIO(pic)
        img = Image.open(stream)
        img = img.resize((900, 600))
        img = ImageTk.PhotoImage(img)
        workoutLabel.config(image=img)
        images.append(img)  # garbage collection
        headingLabel.config(text=workoutResults[count][1])
        repsLabel.config(text=workoutResults[count][2])
        descriptionLabel.config(text=descriptionList[(workoutResults[count][3])])
        weightDropMenu['menu'].delete(0, 'end')
        weightType.set('')
        weightVal.set('')


    workoutLabel = Label(frame, image=img1)
    headingLabel = Label(win, text=workoutResults[0][1], bg='#FFF3C7', font='times 20')
    headingLabel.place(x=400, y=100)
    repsLabel = Label(win, text=workoutResults[0][2], bg='#FBF6F6', font='times 20')
    repsLabel.place(x=500, y=750)
    Button(win, text='DONE', font='times 15', height=4, pady=5, bg='#FFF3C7', command=changeImage).place(x=900, y=0)
    workoutLabel.pack()


    Label(win, text='REPS: ', bg='#FBF6F6', font='times 20').place(x=400, y=750)


    descriptionLabel = Label(win, text=descriptionList[(workoutResults[0][3])], bg='#FBF6F6', font='times 14', justify=CENTER, wraplength=900)
    descriptionLabel.place(x=50, y=800)

    win.mainloop()
