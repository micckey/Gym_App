import asyncio
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkcalendar import Calendar
import io
# from trainee.settings_window import SettingsWindow
# from trainee.workouts import WorkoutsWindow
from trainee.wordings_list import *
import commands


class TraineeDashboard:
    def __init__(self, wind, traineeID, traineeName):
        self.wind = wind
        self.traineeID = traineeID
        self.traineeName = traineeName
        self.root = Toplevel()
        self.root.configure(bg='lightgray')
        self.root.attributes('-fullscreen', True)

        # Header Label Container
        Label(self.root, width=1847, height=144, bg='#C2CCF2').place(x=0, y=0)

        # Gym logo
        gymPic = Image.open("assets/gym.jpg")
        # Resize image
        gymPic.thumbnail((235, 141))
        test = ImageTk.PhotoImage(gymPic)
        # Positioning the image
        label1 = Label(self.root, image=test)
        label1.image = test
        label1.place(x=0, y=0)

        # Daystar logo
        daystarPic = Image.open("assets/daystar.png")
        # Resize image
        daystarPic.thumbnail((235, 141))
        test2 = ImageTk.PhotoImage(daystarPic)
        # Positioning the image
        label2 = Label(self.root, image=test2)
        label2.image = test2
        label2.place(x=142, y=0)

        # User welcome
        self.var = StringVar()
        self.var.set(f'Hello {self.traineeName},\nWelcome back.')
        Label(self.root, textvariable=self.var, bg='#C2CCF2', height=4, width=50, pady=6, font='times 20',
              justify=LEFT).place(x=374, y=0)

        # Timedate info
        self.lab1 = Label(self.root, bg='#C2CCF2', height=4, pady=6, font='times 20')
        self.lab1.place(x=1600, y=0)

        # Log out function
        self.logoutPic = Image.open('assets/logout.png')
        self.logoutPic.thumbnail((137, 141))
        self.test3 = ImageTk.PhotoImage(self.logoutPic)
        # Button(self.root, text='LOG OUT', image=self.test3, command=self.logout).place(x=0, y=938)

        # Left Label Container
        Label(self.root, width=143, height=899, bg='#FBF6F6').place(x=0, y=142)

        # Settings button
        # Button(self.root, text='SETTINGS', width=14, padx=13, height=6, command=self.launch_settings).place(x=0, y=142)

        # Progress button
        Button(self.root, text='PROGRESS', width=14, padx=13, height=6, command='').place(x=0, y=255)

        # Training Container
        Label(self.root, width=1082, height=883, bg='#FFF3C7').place(x=142, y=142)

        # # Heading
        # Label(self.root, text='TODAY\'S TRAINING', bg='#FBF6F6', width=90, padx=4, height=2, font='times 20').place(x=

    def run(self):
            self.wind.mainloop()

if __name__ == '__main__':
    root = Tk()
    dashboard = TraineeDashboard(root, 'trainee_id', 'trainee_name')
    dashboard.run()


# from trainee_dashboard import TraineeDashboard
#
# # create an instance of TraineeDashboard class
# trainee_dashboard = TraineeDashboard(wind, traineeID, traineeName)
#
# # call the show_dashboard() method to display the dashboard
# trainee_dashboard.show_dashboard()