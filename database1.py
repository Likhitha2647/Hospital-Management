import sqlite3
conn=sqlite3.connect('test.db')
conn.execute('''CREATE TABLE HOSPDATA (NAME CHAR(50), EMAIL CHAR(50),AGE INT NOT NULL,GENDER CHAR(10),LOCATION CHAR(100),APPOINTMENT_TIME INT(6),PHONE_NUMBER INT(10),DOCTOR_NAME CHAR(50),PROBLEM CHAR(200));''')
print("done");
conn.close()
