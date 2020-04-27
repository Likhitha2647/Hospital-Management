# update the appointments
from tkinter import *
import tkinter.messagebox 
import sqlite3

#conn = sqlite3.connect('test.db')
#c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)
    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 

        sql = "SELECT NAME,EMAIL,AGE, GENDER, LOCATION,PHONE_NUMBER,APPOINTMENT_TIME,DOCTOR_NAME,PROBLEM FROM HOSPDATA WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[0]
            self.email = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.phone = self.row[5]
            self.time = self.row[6]
            self.doctName = self.row[7]
            self.problem = self.row[8]

            
        # creating the update form
        self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)
        
        self.uemail = Label(self.master, text="Email", font=('arial 18 bold'))
        self.uemail.place(x=0, y=180)

        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=220)

        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=0, y=260)

        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=300)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=340)

        self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
        self.utime.place(x=0, y=380)

        self.udoctName = Label(self.master, text="Doctor Name", font=('arial 18 bold'))
        self.udoctName.place(x=0, y=420)

        self.uproblem = Label(self.master, text="Problem", font=('arial 18 bold'))
        self.uproblem.place(x=0, y=460)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.email))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.age))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END, str(self.gender))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.location))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END, str(self.phone))

        self.ent7 = Entry(self.master, width=30)
        self.ent7.place(x=300, y=380)
        self.ent7.insert(END, str(self.time))

        self.ent8 = Entry(self.master, width=30)
        self.ent8.place(x=300, y=420)
        self.ent8.insert(END, str(self.doctName))

        self.ent9 = Entry(self.master, width=30)
        self.ent9.place(x=300, y=460)
        self.ent9.insert(END, str(self.problem))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=500)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=500)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() 
        self.var3 = self.ent3.get() 
        self.var4 = self.ent4.get() 
        self.var5 = self.ent5.get() 
        self.var6 = self.ent6.get() 
        self.var7 = self.ent7.get()
        self.var8 = self.ent8.get()
        self.var9 = self.ent9.get() 

        query = "UPDATE HOSPDATA SET NAME=?,EMAIL=?, AGE=?, GENDER=?, LOCATION=?, PHONE_NUMBER=?, APPOINTMENT_TIME=?, DOCTOR_NAME=?, PROBLEM=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8,self.var9, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM HOSPDATA WHERE NAME LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        self.ent7.destroy()
        self.ent8.destroy()
        self.ent9.destroy()
# creating the object
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()
