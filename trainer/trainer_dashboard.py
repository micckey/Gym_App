from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
from trainer.trainer_settings import launch


def instructorDash(wind, trainerID, trainerName):
    # root = Tk()
    # root.title('Daystar Gym App')
    # root.configure(width=1440, height=1040)
    # root.attributes('-zoomed', True)
    # root.configure(bg='lightgray')

    win = Toplevel()
    #root.configure(width=1440, height=1040)
    win.configure(bg='lightgray')
    win.resizable(False, False)
    win.attributes('-zoomed', True)


    #Header Label Container
    Label(win, width=1847, height=144, bg='#C2CCF2').place(x=0, y=0)
    #Gym logo
    gymPic = Image.open("assets/gym.jpg")
    #Resize image
    gymPic.thumbnail((235, 141))
    test = ImageTk.PhotoImage(gymPic)
    #Positioning the image
    label1 = Label(win, image=test)
    label1.image = test
    label1.place(x=0, y=0)

    #Daystar logo
    daystarPic = Image.open("assets/daystar.png")
    #Resize image
    daystarPic.thumbnail((235, 141))
    test2 = ImageTk.PhotoImage(daystarPic)
    #Positioning the image
    label2 = Label(win, image=test2)
    label2.image = test2
    label2.place(x=142, y=0)





    #User welcome
    var = StringVar()
    var.set('Hello Coach '+trainerName+', \nWelcome back. ')
    Label(win, textvariable=var, bg='#C2CCF2', height=4, width=50, pady=6, font='times 20', justify=LEFT).place(x=374, y=0)
    #Timedate info
    lab1 = Label(win, bg='#C2CCF2', height=4, pady=6, font='times 20')
    lab1.place(x=1600, y=0)

    def digitalclock():
        text_input = time.strftime("%H:%M %p \n%a, %d %b %Y ")
        lab1.config(text=text_input)
        lab1.after(1000, digitalclock)

    digitalclock()



    #Log out function
    def popup():
      response = messagebox.askquestion(parent=win, message=" Are you sure? \n Exit Program ?", icon='warning')
      if response == "yes":
          win.destroy()
          wind.deiconify()
      else:
           print('Thank you for Staying')



    #Left Label Container
    Label(win, width=143, height=899, bg='#FBF6F6').place(x=0, y=142)
    #Settings button
    Button(win, text='SETTINGS', width=14, padx=13, height=6, command=launch).place(x=0, y=142)
    #Logout button
    logoutPic = Image.open('assets/logout.png')
    logoutPic.thumbnail((137, 141))
    test3 = ImageTk.PhotoImage(logoutPic)
    Button(win, text='LOG OUT', image=test3, command=popup).place(x=0, y=872)


    #Dataset Container
    datasetFrame = LabelFrame(win, width=1704, height=873, bg='#FBF6F6')
    datasetFrame.place(x=142, y=143)




    win.mainloop()