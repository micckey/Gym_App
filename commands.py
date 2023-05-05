import asyncio
from tkinter import messagebox
from trainee.trainee_dashboard import traineeDash
from trainer.trainer_dashboard import instructorDash
from tkinter import *
from mysql.connector import Error
from mysql.connector import pooling

#Normal connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="owen",
#     password="ichimaruGin",
#     port="3306",
#     database="Daystar_Gym_App"
# )
#
# mycursor = mydb.cursor()

#Connection Pool
conn_pool = pooling.MySQLConnectionPool(
    pool_name='gym_pool',
    pool_size=5,
    pool_reset_session=True,
    host="localhost",
    user="owen",
    password="ichimaruGin",
    port="3306",
    database="Daystar_Gym_App"
)


# register trainee
def regTrainee(win, fname, lname, weight, fitgoal, passw):
    mydb = conn_pool.get_connection()
    mycursor = mydb.cursor()
    async def insertToUsers():
        await insertToTrainee()
        traineeID = mycursor.lastrowid
        sql2 = 'UPDATE Users SET Users_password=%s WHERE Users_id=%s'
        adr2 = (passw, traineeID)
        try:
            if mydb.is_connected():
                mycursor.execute(sql2, adr2)
                mydb.commit()
                print('Data inserted to Users successfully')
        except Error as e:
            mydb.rollback()
            print('Data insertion to Users failed using connection pool: ', e)
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed at Trainee registration Instance")
                messg = ('Registration Successful!!\n' + 'Your ID is: ' + str(
                    traineeID) + '\n' + 'You may proceed to log in ' + fname)
                messagebox.showinfo(parent=win, message=messg)
                win.destroy()

    async def insertToTrainee():
        sql1 = "SELECT Instructors_id FROM Instructors where Instructors_speciality=%s"
        val2 = [(fitgoal)]
        mycursor.execute(sql1, val2)
        instID = mycursor.fetchone()[0]
        sql = 'INSERT INTO Trainee (Trainee_fname, Trainee_lname, Trainee_weight, Trainee_fitness_goal, Instructors_Instructors_id) VALUES (%s,%s,%s,%s,%s)'
        val = (fname, lname, weight, fitgoal, instID)

        try:
            if mydb.is_connected():
                mycursor.execute(sql, val)
                mydb.commit()
                print('Data inserted to Trainee successfully')
        except Error as e:
            mydb.rollback()
            print('Data insertion to Trainee failed using connection pool ', e)

    asyncio.run(insertToUsers())


# register instructor
def regInstructor(win, fname, lname, specs, pic, passw):
    mydb = conn_pool.get_connection()
    mycursor = mydb.cursor()
    async def insertToUsers():
        await insertToInstructors()
        instrID = mycursor.lastrowid
        sql2 = 'update Users set Users_password=%s where Users_id=%s'
        adr2 = (passw, instrID)
        try:
            if mydb.is_connected():
                mycursor.execute(sql2, adr2)
                mydb.commit()
                print('Data inserted to Users successfully')
        except Error as e:
            mydb.rollback()
            print('Data insertion to Users failed using connection pool ', e)
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed at Instructor Registration Instance")
                messg = ('Registration Successful!!\n' + 'Your ID is: ' + str(
                    instrID) + '\n' + 'You may proceed to log in ' + fname)
                messagebox.showinfo(parent=win, message=messg)
                win.destroy()

    async def insertToInstructors():
        sql = 'INSERT INTO Instructors (Instructors_fname, Instructors_lname, Instructors_speciality, Instructors_pict) VALUES (%s,%s,%s,%s)'
        val = (fname, lname, specs, pic)
        try:
            if mydb.is_connected():
                mycursor.execute(sql, val)
                mydb.commit()
                print('Data inserted to instructors successfully')
        except Error as e:
            mydb.rollback()
            print('Data insertion to Instructors failed using connection pool ', e)

    asyncio.run(insertToUsers())

# fetch data and password of trainee
def loadScreen(wind, userid, uname):
    if int(userid) > 1000:
        traineeDash(wind, userid, uname)
    else:
        instructorDash(wind, userid, uname)

def loginFunc(win, entryPass, userid, passw):
    if userid == "" or passw == "":
        messagebox.showerror("ERROR!!", "Blank not allowed!!!")
    else:
        mydb = conn_pool.get_connection()
        mycursor = mydb.cursor()
        sql1 = "SELECT Users_name, Users_password FROM Users where Users_id=%s"
        val2 = [(userid)]
        mycursor.execute(sql1, val2)
        result = mycursor.fetchone()
        username = result[0]
        password = result[1]

        if passw == password:
            messagebox.showinfo("SUCCESS!!", "Login Successful, \n WELCOME: "+username)
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed at Login Instance")
            win.withdraw()
            entryPass.delete(0, END)

            #Load trainee and instructors dashboard
            loadScreen(win, userid, username)

        else:
            messagebox.showwarning("ERROR!!", "Incorrect ID and/or Password \n Try Again")


#Get Workouts Screen
# select workouts
async def selectFunc(trID):
    mydb = conn_pool.get_connection()
    mycursor = mydb.cursor()
    fitgoal = await loadWorkouts(trID)
    try:
        if mydb.is_connected():
            sql = "SELECT Workouts_pict, Workouts_name, Workouts_reps, Workouts_id FROM Workouts WHERE Workouts_category= %s"
            val = [(fitgoal)]
            mycursor.execute(sql, val)
            result = mycursor.fetchall()
        return result

    except Error as e:
        print('Error while connecting to MySQL using connection pool ', e)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print('MySQL connection closed at Loading workouts instance')

# load workouts
async def loadWorkouts(userid):
    mydb = conn_pool.get_connection()
    mycursor = mydb.cursor()
    try:
        if mydb.is_connected():
            sql1 = 'select Trainee_fitness_goal from Trainee where Trainee_id = %s'
            val2 = [(userid)]
            mycursor.execute(sql1, val2)
            values = mycursor.fetchone()
            goal = values[0]
            if goal == 'Keeping Fit':
                fitgoal = 'Fitness'
            elif goal == 'Weight Management':
                fitgoal = 'Weight'


        return fitgoal
    except Error as e:
        print('Error while connecting to MySQL using connnection pool ', e)



# load instructors info
async def loadInstructorsInfo(trnID):
    mydb = conn_pool.get_connection()
    mycursor = mydb.cursor()
    fitgoal = await getGoal(trnID)
    try:
        if mydb.is_connected():
            sql1 = 'select Instructors_pict, Instructors_fname, Instructors_id from Instructors where Instructors_speciality = %s'
            val2 = [(fitgoal)]
            mycursor.execute(sql1, val2)
            result = mycursor.fetchall()
        return result
    except Error as e:
        print('Error while connecting to MySQL using connection pool ', e)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print('MySQL connection closed at Loading Instructor\'s info instance')

async def getGoal(usID):
    mydb = conn_pool.get_connection()
    mycursor = mydb.cursor()
    try:
        if mydb.is_connected():
            sql1 = 'select Trainee_fitness_goal from Trainee where Trainee_id = %s'
            val2 = [(usID)]
            mycursor.execute(sql1, val2)
            values = mycursor.fetchone()
            goal = values[0]
        return goal
    except Error as e:
        print('Error while connecting to MySQL using connection pool ', e)

#Select an Instructor
def selectInstructor(win, trnID, instID, instName):
    mydb = conn_pool.get_connection()
    mycursor = mydb.cursor()
    sql2 = 'UPDATE Trainee SET Instructors_Instructors_id=%s WHERE Trainee_id=%s'
    adr2 = [instID, trnID]
    try:
        if mydb.is_connected():
            mycursor.execute(sql2, adr2)
            mydb.commit()
            print('Instructor ID updated successfully')
    except Error as e:
        mydb.rollback()
        print('Data insertion to Users failed using connection pool: ', e)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            messg = ('You have now selected Coach ' + instName)
            messagebox.showinfo(parent=win, message=messg)

# load registered trainees on instructor's dashboard
# load dates worked out
