import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="owen",
    password="ichimaruGin",
    port="3306",
    database="Daystar_Gym_App"
)

mycursor = mydb.cursor()
from tkinter import messagebox

import login
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkcalendar import Calendar
from trainee.settings_window import launch
from trainee.workouts import launch2
import io
import PIL.Image
import time


class GUI(Tk):
    def __int__(self, master):
        # root.configure(width=1440, height=1040)
        #self.configure(bg='lightgray')
        # root.resizable(False, False)
        # root.overrideredirect(1)
        #self.attributes('-fullscreen', True)
        self.master = master
        self.button1 = Button(self.frame, text='New Window', width=25, command=self.new_window)
        self.button1.pack()

    def newWindow(self):
        self.newWin = Toplevel(self.master)
        self.configure(bg='lightgray')
        self.attributes('-fullscreen', True)
        self.app = GUI2(self.newWin)
        #window = GUI2()
        #window.mainloop()

class GUI2(Toplevel):
    # Header Label Container

    def topBar(self):
        # User welcome
        var = StringVar()
        var.set('Hello Jeremy, \nWelcome back. ')
        Label(self, textvariable=var, bg='#C2CCF2', height=4, width=50, pady=6, font='none 20', justify=LEFT).place(
            x=374, y=0)
        # Timedate info

        self.lab1 = Label(self, font='times 20', bg='#C2CCF2')
        self.lab1.place(x=1600, y=0)

        def digitalclock(self):
            text_input = time.strftime("%H:%M %p \n%a, %d %b %Y ")
            self.lab1.config(text=text_input)
            self.lab1.after(1000, digitalclock)

        digitalclock()

        # digitalclock()
        # Log out function
        def popup(self):
            response = messagebox.askquestion("Daystar Gym App ", "Exit Programe ?",
                                              icon='warning')
            # print(response)
            if response == "yes":
                self.destroy()
                login.launch()
            else:
                print('Thank you for Staying')

        # Left Label Container

        # Settings button
        Button(self, text='SETTINGS', width=14, padx=13, height=6, command=launch).place(x=0, y=142)
        # Logout button

        Button(self, text='LOG OUT', command=popup).place(x=0, y=872)

    def trainBar(self):
        # Training Container
        # Heading
        Label(self, text='Todays Training', bg='#FBF6F6', width=63, padx=4, height=1, pady=12, font='none 20').place(
            x=142, y=142)

        fitgoal = 'Weight'
        sql1 = "SELECT Workouts_pict FROM Workouts where Workouts_category=%s"
        val2 = [(fitgoal)]
        mycursor.execute(sql1, val2)
        result = mycursor.fetchall()
        # pic = result[3]

        # Label(root, width=1082, height=883, bg='#FBF6F6').place(x=142, y=142)
        frame = Frame(self, width=1082, height=515, bg='#FFF3C7')
        frame.place(x=185, y=200)
        frame.pack_propagate(False)

        def getPics():
            return result

        pics = getPics()
        images = []
        c = 0
        r = 0
        for j in range(6):

            pic = pics[j][0]
            stream = io.BytesIO(pic)
            # stream= io.StringIO(pic)
            img = PIL.Image.open(stream)
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

        # View more button

        Button(self, text='View More', height=200, width=100, command=launch2).place(x=1030, y=360)
        # view more label
        Label(self, text='VIEW MORE', bg='#FFF3C7', height=1, font='none 12').place(x=1034, y=570)

    def recBar(self):
        # Recommendations container

        var3 = StringVar()
        var3.set('Recommended food \nAvocado Salad: ')
        Label(self, textvariable=var3, bg='#C2CCF2', font='none 14').place(x=142, y=727)
        # Food thumbnail

        # Random quote

        # Calender container

    def calBar(self):
        # Calender Heading
        Label(self, text='CALENDER', bg='lightgray', width=36, padx=6, height=2, font='none 20').place(x=1222, y=142)
        # Add the Calendar module
        todayDate = datetime.now()
        cal = Calendar(self, selectmode='day',
                       year=todayDate.year, month=todayDate.month,
                       day=todayDate.day, font='Comic_Sans_MS, 23').place(x=1222, y=210)
        Button(self, text='VIEW HISTORY', width=16, padx=13, height=3, font='none 12', command='').place(x=1440, y=600)

    def instBar(self):
        # Instructors' container
        # Thumbnail 1
        Label(self, text='Pic 1', bg='lightgray', width=10, height=5, font='none 20').place(x=1240, y=750)
        # Button
        Button(self, text='Coach Ron', width=14, padx=13, height=2, command='').place(x=1254, y=925)
        # Thumbnail 1
        Label(self, text='Pic 2', bg='lightgray', width=10, height=5, font='none 20').place(x=1440, y=750)
        # Button
        Button(self, text='Coach Ben', width=14, padx=13, height=2, command='').place(x=1454, y=925)
        # Thumbnail 1
        Label(self, text='Pic 2', bg='lightgray', width=10, height=5, font='none 20').place(x=1640, y=750)
        # Button
        Button(self, text='Coach Martin', width=14, padx=13, height=2, command='').place(x=1654, y=925)


if __name__ == '__main__':
    window = GUI()
    window.mainloop()
