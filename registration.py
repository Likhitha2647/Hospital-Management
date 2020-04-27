from tkinter import *
import sqlite3
import tkinter.messagebox

root = Tk()
root.geometry('800x800')
root.title("Registration Form")


fullName=StringVar()
eml=StringVar()
a = StringVar()
prob=StringVar()
dName=StringVar()
phno = IntVar()
loc= StringVar()
gen=StringVar()
app=IntVar()

# empty list to later append the ids from the database
ids = []

def database():
   
   name1=fullName.get()
   email=eml.get()
   gender=gen.get()
   age=a.get()
   problem=prob.get()
   doctname=dName.get()
   location=loc.get()
   apptime=app.get()
   phoneno=phno.get()
   conn = sqlite3.connect('test.db')
   cursor=conn.cursor()

   if name1 == '' or email == '' or gender == '' or age == '' or problem == '' or location == '' or apptime == '' or doctname == '' or phoneno =='':
       tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
   else:
       # now we add to the database
       sql="INSERT INTO HOSPDATA (NAME,EMAIL,AGE,GENDER, LOCATION,APPOINTMENT_TIME,PHONE_NUMBER,DOCTOR_NAME,PROBLEM) VALUES(?,?,?,?,?,?,?,?,?)"
       cursor.execute(sql, (name1, email,age,gender,location,apptime,phoneno,doctname,problem)) 
       conn.commit()
       tkinter.messagebox.showinfo("Success", "Appointment for " +str(name1) + " has been created" )
   # getting the number of appointments fixed to view in the log
  #result = cursor.execute(sql2)
   #for row in result:
    #   ids = row[0]
     #  ids.append(ids)
   # ordering the ids
  # new = sorted(ids)
   #final_id = new[len(ids)-1]
   #print("Total Appointments till now :  " + str(final_id))

   
   
  
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FULL NAME",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=fullName)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="EMAIL",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=eml)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="GENDER",width=20,font=("bold", 10))
label_3.place(x=80,y=230)

Radiobutton(root, text="MALE", value="male", var=gen).place(x=235,y=230)
Radiobutton(root, text="FEMALE", value="female", var=gen).place(x=290,y=230)

#Radiobutton(root, text="Male",padx = 5,variable=gen, value='m').place(x=235,y=230)
#Radiobutton(root, text="Female",padx = 20,variable=gen, value='f').place(x=290,y=230)

label_4 = Label(root, text="DOCTOR NAME",width=20,font=("bold", 10))
label_4.place(x=80,y=280)

list1 = ['DR RAMA','DR T S MOHAN','DR ABBAI','DR PEDDAVEERA RAJU','DR RAMESH','DR VIJETHA'];

droplist=OptionMenu(root,dName, *list1)
droplist.config(width=25)
dName.set('select your doctor') 
droplist.place(x=240,y=280)

label_5 = Label(root, text="PROBLEM",width=20,font=("bold", 10))
label_5.place(x=80,y=330)

entry_5 = Entry(root,textvar=prob)
entry_5.place(x=240,y=330)


label_6 = Label(root, text="AGE",width=20,font=("bold", 10))
label_6.place(x=80,y=380)

entry_6 = Entry(root,textvar=a)
entry_6.place(x=240,y=380)

label_7 = Label(root, text="APPOINTMENT TIME",width=20,font=("bold", 10))
label_7.place(x=80,y=420)

entry_7 = Entry(root,textvar=app)
entry_7.place(x=240,y=420)

label_8 = Label(root, text="PHONE NUMBER",width=20,font=("bold", 10))
label_8.place(x=80,y=470)

entry_8 = Entry(root,textvar=phno)
entry_8.place(x=240,y=470)

label_9 = Label(root, text="LOCATION",width=20,font=("bold", 10))
label_9.place(x=80,y=520)

entry_9 = Entry(root,textvar=loc)
entry_9.place(x=240,y=520)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=220,y=570)

root.mainloop()
























