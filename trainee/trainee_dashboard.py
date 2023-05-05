import asyncio
from tkinter import messagebox
import commands
import time
from trainee.wordings_list import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkcalendar import Calendar
from trainee.settings_window import launch
from trainee.workouts import launch2
import io


def traineeDash(wind, traineeID, traineeName):
    # root = Tk()
    # root.title('Daystar Gym App')
    # root.configure(width=1440, height=1040)
    # root.attributes('-zoomed', True)
    # root.configure(bg='lightgray')

    root = Toplevel()
    #root.configure(width=1440, height=1040)
    root.configure(bg='lightgray')
    #root.resizable(False, False)
    root.attributes('-fullscreen', True)
    #root.overrideredirect(1)


    #Header Label Container
    Label(root, width=1847, height=144, bg='#C2CCF2').place(x=0, y=0)
    #Gym logo
    gymPic = Image.open("assets/gym.jpg")
    #Resize image
    gymPic.thumbnail((235, 141))
    test = ImageTk.PhotoImage(gymPic)
    #Positioning the image
    label1 = Label(root, image=test)
    label1.image = test
    label1.place(x=0, y=0)

    #Daystar logo
    daystarPic = Image.open("assets/daystar.png")
    #Resize image
    daystarPic.thumbnail((235, 141))
    test2 = ImageTk.PhotoImage(daystarPic)
    #Positioning the image
    label2 = Label(root, image=test2)
    label2.image = test2
    label2.place(x=142, y=0)

    #User welcome
    var = StringVar()
    var.set('Hello '+traineeName+', \nWelcome back. ')
    Label(root, textvariable=var, bg='#C2CCF2', height=4, width=50, pady=6, font='times 20', justify=LEFT).place(x=374, y=0)
    #Timedate info
    lab1 = Label(root, bg='#C2CCF2', height=4, pady=6, font='times 20')
    lab1.place(x=1600, y=0)
    def digitalclock():
        text_input = time.strftime("%H:%M %p \n%a, %d %b %Y ")
        lab1.config(text=text_input)
        lab1.after(200, digitalclock)
    digitalclock()



    #Log out function
    def popup():
      response = messagebox.askquestion("Daystar Gym App ", "Exit Program?",
      icon='warning')
      if response == "yes":
          root.destroy()
          wind.deiconify()
      else:
           print('Thank you for Staying')

    #Left Label Container
    Label(root, width=143, height=899, bg='#FBF6F6').place(x=0, y=142)
    #Settings button
    Button(root, text='SETTINGS', width=14, padx=13, height=6, command=launch).place(x=0, y=142)
    #Progrss button
    Button(root, text='PROGRESS', width=14, padx=13, height=6, command='').place(x=0, y=255)
    #Logout button
    logoutPic = Image.open('assets/logout.png')
    logoutPic.thumbnail((137, 141))
    test3 = ImageTk.PhotoImage(logoutPic)
    Button(root, text='LOG OUT', image=test3, command=popup).place(x=0, y=938)



    #Training Container
    Label(root, width=1082, height=883, bg='#FFF3C7').place(x=142, y=142)
    #Heading
    Label(root, text='TODAY\'S TRAINING', bg='#FBF6F6', width=90, padx=4, height=2, font='times 20').place(x=142, y=142)

    #Thumbnails container

    frame = Frame(root, width=1082, height=883, bg='#FFF3C7')
    frame.place(x=185, y=210)
    frame.pack_propagate(False)

    workoutResults = asyncio.run(commands.selectFunc(traineeID))

    images = []
    c = 0
    r = 0
    for j in range(6):
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

    #View more button
    viemorePic = Image.open('assets/next.png')
    viemorePic = viemorePic.resize((100, 200), Image.Resampling.LANCZOS)
    test4 = ImageTk.PhotoImage(viemorePic)
    Button(root, text='View More', image=test4, height=200, width=100, command=lambda: launch2(workoutResults)).place(x=1030, y=360)
    #view more label
    Label(root, text='VIEW MORE', bg='#FFF3C7', height=1, font='times 12').place(x=1034, y=570)



    #Recommendations container
    Label(root, width=1082, height=288, bg='#C2CCF2').place(x=142, y=750)
    var3 = StringVar()
    var3.set('Recommended food:')
    Label(root, textvariable=var3, bg='#C2CCF2', font='times 16').place(x=142, y=760)
    #Food thumbnail
    foodPic = Image.open(random_food)
    #Resize image
    foodPic = foodPic.resize((230, 230), Image.Resampling.LANCZOS)
    test5 = ImageTk.PhotoImage(foodPic)
    #Positioning the image
    label3 = Label(root, image=test5)
    label3.image = random_food
    label3.place(x=142, y=808)
    #Random quote
    var4 = StringVar()
    var4.set(random_quote)
    Label(root, textvariable=var4, bg='#C2CCF2', justify=CENTER, wraplength=800, font='times 18').place(x=379, y=808)



    #Calender container
    Frame(root, width=625, height=608, bg='#FBF6F6', ).place(x=1222, y=142)
    #Calender Heading
    Label(root, text='CALENDER', bg='lightgray', width=47, padx=6, height=2, font='times 20').place(x=1222, y=142)
    # Add the Calendar module
    todayDate = datetime.now()
    cal = Calendar(root, selectmode='day',
             year=todayDate.year, month=todayDate.month,
             day=todayDate.day, font='Comic_Sans_MS, 23')
    cal.place(x=1222, y=210)
    Button(root, text='VIEW HISTORY', width=16, padx=13, height=3, font='times 12', command='').place(x=1440, y=600)




    #Instructors' container
    frame2 = Frame(root, width=625, height=288, bg='#FBF6F6')
    frame2.place(x=1222, y=760)
    frame2.pack_propagate(False)
    instructorResults = asyncio.run(commands.loadInstructorsInfo(traineeID))
    images2 = []
    c = 0
    r = 0
    for i in range(len(instructorResults)):
        pic2 = instructorResults[i][0]
        stream2 = io.BytesIO(pic2)
        img2 = Image.open(stream2)
        img2 = img2.resize((180, 180))
        img2 = ImageTk.PhotoImage(img2)
        e = Label(frame2, image=img2)
        eb = Button(frame2, text=f'Coach {instructorResults[i][1]}', command=lambda: commands.selectInstructor(root, traineeID, instructorResults[i][2], instructorResults[i][1]))
        e.grid(row=r, column=c, ipady=7, ipadx=7)
        eb.grid(row=r+1, column=c, ipadx=7, ipady=7)
        images2.append(img2)  # garbage collection
        if c == 2:
            r += 1
            c = 0
        else:
            c += 1


    root.mainloop()