from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile


from PIL import Image, ImageTk

import commands
from commands import *


class InstructorsRegistration:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.configure(width=840, height=1040)
        self.top.configure(bg='#FBF6F6')
        self.top.resizable(False, False)

        screen_width = self.top.winfo_screenwidth()  # Width of the screen
        screen_height = self.top.winfo_screenheight()  # Height of the screen
        x = (screen_width / 2) - (840 / 2)
        y = (screen_height / 2) - (1040 / 2)
        w = 840
        h = 1040
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))

        Label(self.top, text='REGISTER', bg='#C2CCF2', font='none 20', width=50, height=3).place(x=0, y=0)

        global entryFName
        global entryLName
        global entrySpeciality
        # global entryPic
        global entryPass
        Label(self.top, text="First Name:", font='none 16').place(x=20, y=200)
        Label(self.top, text="Last Name:", font='none 16').place(x=20, y=300)
        Label(self.top, text="Speciality:", font='none 16').place(x=20, y=400)
        Label(self.top, text="Pic:", font='none 16').place(x=20, y=500)
        Label(self.top, text="Password:", font='none 16').place(x=20, y=700)
        entryFName = Entry(self.top, bd=5, width=20, font='none 30')
        entryFName.place(x=160, y=200)
        entryLName = Entry(self.top, bd=5, width=20, font='none 30')
        entryLName.place(x=160, y=300)

        options = ['Keeping Fit', 'Weight Management', 'Martial Arts']
        # datatype of menu text
        entrySpeciality = StringVar(self.top)
        # initial menu text
        entrySpeciality.set('')
        # Create Dropdown menu
        drop = OptionMenu(self.top, entrySpeciality, *options).place(x=160, y=400)

        # image picker

        Button(self.top, text='Upload Image', width=20, command=self.uploadFile).place(x=160, y=500)

        entryPass = Entry(self.top, bd=5, width=20, font='none 30', show='*')
        entryPass.place(x=160, y=700)

        # insertVal=regInstructor(entryFName, entryLName, entrySpeciality, entryPic, entryPass)

        self.entryPic = None
        self.filename = None
        self.img = None

        Button(self.top, text="SIGN UP",
               command=lambda: commands.regInstructor(self.top, entryFName.get(), entryLName.get(),
                                                      entrySpeciality.get(),
                                                      self.convBin(self.filename), entryPass.get()), height=3, width=20, bd=6,
               bg='#FFF3C7').place(x=320, y=800)

        self.top.mainloop()

    def uploadFile(self):

        # ftypes = [('Jpg Files', '*.jpg'), ('Png Files', '*.png')]
        # filename = filedialog.askopenfilename(parent=self.top, filetypes=ftypes)
        # img = Image.open(filename)

        self.filename = filedialog.askopenfilename(parent=self.top,
                                                filetypes=[('Jpg Files', '*.jpg'), ('Png Files', '*.png')])
        from PIL import Image
        self.img = Image.open(self.filename)

        self.img = self.img.resize((180, 180), Image.Resampling.LANCZOS)
        self.entryPic = ImageTk.PhotoImage(self.img)

        # Resize image
        # img = img.resize((180, 180), Image.Resampling.LANCZOS)
        # entryPic = ImageTk.PhotoImage(img)

        # img = img.resize((230, 230))  # new width & height
        # test5 = ImageTk.PhotoImage(img)

        # Positioning the image
        labl = Label(self.top, image=self.entryPic)
        labl.place(x=400, y=500)
        labl.image = self.entryPic
        labl['image'] = self.entryPic

    def convBin(self, fileName):
        self.fileName = fileName
        file = open(fileName, 'rb')
        binaryData = file.read()
        return binaryData


class TraineeRegistration:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.configure(width=840, height=1040)
        self.top.configure(bg='#FBF6F6')
        self.top.resizable(False, False)

        screen_width = self.top.winfo_screenwidth()  # Width of the screen
        screen_height = self.top.winfo_screenheight()  # Height of the screen
        x = (screen_width / 2) - (840 / 2)
        y = (screen_height / 2) - (1040 / 2)
        w = 840
        h = 1040
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))

        Label(self.top, text='REGISTER', bg='#C2CCF2', font='none 20', width=50, height=3).place(x=0, y=0)

        global entryFName
        global entryLName
        global entryWeight
        global entryFitnessGoal
        global entryPass
        Label(self.top, text="First Name:", font='none 16').place(x=20, y=200)
        Label(self.top, text="Last Name:", font='none 16').place(x=20, y=300)
        Label(self.top, text="Weight:", font='none 16').place(x=20, y=400)
        Label(self.top, text="Fitness Goal:", font='none 16').place(x=20, y=500)
        Label(self.top, text="Password:", font='none 16').place(x=20, y=650)
        entryFName = Entry(self.top, bd=5, width=20, font='none 30')
        entryFName.place(x=160, y=200)
        entryLName = Entry(self.top, bd=5, width=20, font='none 30')
        entryLName.place(x=160, y=300)
        entryWeight = Entry(self.top, bd=5, width=20, font='none 30')
        entryWeight.place(x=160, y=400)

        options = ['Keeping Fit', 'Weight Management', 'Martial Arts']
        # datatype of menu text
        entryFitnessGoal = StringVar(self.top)
        # initial menu text
        entryFitnessGoal.set('')
        # Create Dropdown menu
        drop = OptionMenu(self.top, entryFitnessGoal, *options).place(x=160, y=500)

        entryPass = Entry(self.top, bd=5, width=20, font='none 30', show='*')
        entryPass.place(x=160, y=650)

        Button(self.top, text="SIGN UP",
               command=lambda: commands.regTrainee(self.top, entryFName.get(), entryLName.get(), entryWeight.get(),
                                                   entryFitnessGoal.get(), entryPass.get()), height=3, width=20, bd=6,
               bg='#FFF3C7').place(x=320, y=750)
        self.top.mainloop()

# def traineeReg_Func():
#     # root = Tk()
#     # root.title('Daystar Gym App')
#     # root.configure(width=840, height=1040)
#     # root.configure(bg='#FBF6F6')
#     # root.eval('tk::PlaceWindow . center')
#
#     root = Toplevel()
#     root.configure(width=840, height=1040)
#     root.configure(bg='#FBF6F6')
#     root.resizable(False, False)
#     # win.overrideredirect(1)
#     # win.eval('tk::PlaceWindow . center')
#     # position screen
#     screen_width = root.winfo_screenwidth()  # Width of the screen
#     screen_height = root.winfo_screenheight()  # Height of the screen
#     # Calculate Starting X and Y coordinates for Window
#     x = (screen_width / 2) - (840 / 2)
#     y = (screen_height / 2) - (1040 / 2)
#     w = 840
#     h = 1040
#     root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#
#     Label(root, text='REGISTER', bg='#C2CCF2', font='none 20', width=50, height=3).place(x=0, y=0)
#
#     global entryFName
#     global entryLName
#     global entryWeight
#     global entryFitnessGoal
#     global entryPass
#     Label(root, text="First Name:", font='none 16').place(x=20, y=200)
#     Label(root, text="Last Name:", font='none 16').place(x=20, y=300)
#     Label(root, text="Weight:", font='none 16').place(x=20, y=400)
#     Label(root, text="Fitness Goal:", font='none 16').place(x=20, y=500)
#     Label(root, text="Password:", font='none 16').place(x=20, y=650)
#     entryFName = Entry(root, bd=5, width=20, font='none 30')
#     entryFName.place(x=160, y=200)
#     entryLName = Entry(root, bd=5, width=20, font='none 30')
#     entryLName.place(x=160, y=300)
#     entryWeight = Entry(root, bd=5, width=20, font='none 30')
#     entryWeight.place(x=160, y=400)
#
#     # Entry(root, bd=5, width=20, font='none 30', show='*')
#
#     options = ['Keeping Fit', 'Weight Management', 'Martial Arts']
#     # datatype of menu text
#     entryFitnessGoal = StringVar(root)
#     # initial menu text
#     entryFitnessGoal.set('')
#     # Create Dropdown menu
#     drop = OptionMenu(root, entryFitnessGoal, *options).place(x=160, y=500)
#
#     entryPass = Entry(root, bd=5, width=20, font='none 30', show='*')
#     entryPass.place(x=160, y=650)
#
#     Button(root, text="SIGN UP",
#            command=lambda: commands.regTrainee(root, entryFName.get(), entryLName.get(), entryWeight.get(),
#                                                entryFitnessGoal.get(), entryPass.get()), height=3, width=20, bd=6,
#            bg='#FFF3C7').place(x=320, y=750)
#     root.mainloop()
