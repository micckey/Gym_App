
from tkinter import *
from register_screens import *
from commands import *
from register_screens import *



# instructorReg_Func = InstructorsRegistration()



class LaunchScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title('Daystar Gym App')
        self.root.configure(width=840, height=1040)
        self.root.configure(bg='#FBF6F6')
        self.root.eval('tk::PlaceWindow . center')

        Label(self.root, text='LOGIN', bg='#C2CCF2', font='none 20', width=50, height=3).place(x=0, y=0)

        Label(self.root, text="User ID:", font='none 16').place(x=20, y=300)
        Label(self.root, text="Password:", font='none 16').place(x=20, y=400)
        self.entryUser = Entry(self.root, bd=5, width=20, font='none 30')
        self.entryUser.place(x=160, y=300)
        self.entryPass = Entry(self.root, bd=5, width=20, font='none 30', show='*')
        self.entryPass.place(x=160, y=400)

        Button(self.root, text="LOGIN", command=self.loginFunc, height=3, width=20, bd=6, bg='#FFF3C7').place(x=320, y=500)

        Label(self.root, text="Don't have an account? Sign up below", font='none 16', wraplength='250').place(x=325, y=600)
        Button(self.root, text="Instructor", command=self.instructorReg_Func, height=3, width=20, bd=6, bg='#FFF3C7').place(x=200, y=700)
        Button(self.root, text="Trainee", command=self.traineeReg_Func, height=3, width=20, bd=6, bg='#FFF3C7').place(x=420, y=700)

        self.root.mainloop()

    def loginFunc(self):
        loginFunc(self.root, self.entryPass, self.entryUser.get(), self.entryPass.get())

    def instructorReg_Func(self):
        InstructorsRegistration(self.root)

    def traineeReg_Func(self):
        TraineeRegistration(self.root)

#
# def launch():
#     root = Tk()
#     root.title('Daystar Gym App')
#     root.configure(width=840, height=1040)
#     root.configure(bg='#FBF6F6')
#     root.eval('tk::PlaceWindow . center')
#
#     Label(root, text='LOGIN', bg='#C2CCF2', font='none 20', width=50, height=3).place(x=0, y=0)
#
#
#     Label(root, text="User ID:", font='none 16').place(x=20, y=300)
#     Label(root, text="Password:", font='none 16').place(x=20, y=400)
#     entryUser = Entry(root, bd=5, width=20, font='none 30')
#     entryUser.place(x=160, y=300)
#     entryPass = Entry(root, bd=5, width=20, font='none 30', show='*')
#     entryPass.place(x=160, y=400)
#
#     Button(root, text="LOGIN", command=lambda: commands.loginFunc(root, entryPass, entryUser.get(), entryPass.get()), height=3, width=20, bd=6, bg='#FFF3C7').place(x=320, y=500)
#
#     Label(root, text="Don't have an account? Sign up below", font='none 16', wraplength='250').place(x=325, y=600)
#     Button(root, text="Instructor", command=register_screens.instructorReg_Func, height=3, width=20, bd=6, bg='#FFF3C7').place(x=200, y=700)
#     Button(root, text="Trainee", command=register_screens.traineeReg_Func, height=3, width=20, bd=6, bg='#FFF3C7').place(x=420, y=700)
#
#
#
#     root.mainloop()
