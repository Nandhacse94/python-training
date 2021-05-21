# 
##1.add stud
##2.cal perc
##3.gener repor
##4.send repo
##
##1
##roll
##name
##mat sci com
##
##2
##
##roll num to fetch
##
##3
##
##gener repo
##
##add perc + status(pass/fail)

## dup roll shouldnt be there
## marks valid bw 1 to 100
## name valid


import sqlite3
import csv
import smtplib
import getpass

db = sqlite3.connect("student_db.sqlite")

try:
    db.execute("create table student(roll integer, name text, maths integer, physics integer, chemistry integer)")
except:
    pass #print("************ Already Table exists! ************")

def checkRoll(num):
    try:
        f = open("student_db.csv","r")
        data = list(csv.reader(f))
        
        for i in data:
            if int(i[0]) == num:
                return True
        return False
    except:
        pass
    finally:
        f.close()

def addData():
    roll = int(input("Enter RollNumber:"))
    
    while roll < 1 or checkRoll(roll):
        print("Invalid Value! please enter roll number above 1")
        roll = int(input("Enter RollNumber:"))

    name = input("Enter the Name of Student:")
    while name.isalpha() == False:
        print("Invalid Value! please enter valid Name")
        name = input("Enter the Name of Student:")
        
    maths = int(input("Enter Maths Marks:"))
    while maths < 0 or maths > 100:
        print("Invalid Value! please enter marks bw 0 to 100")
        maths = int(input("Enter Maths Marks:"))
        
    phy = int(input("Enter Physics Marks:"))
    while phy < 0 or phy > 100:
        print("Invalid Value! please enter marks bw 0 to 100")
        phy = int(input("Enter Physics Marks:"))
        
    che = int(input("Enter Chemistry Marks:"))
    while phy < 0 or phy > 100:
        print("Invalid Value! please enter marks bw 0 to 100")
        che = int(input("Enter Chemistry Marks:"))

    list1 = [roll,name,maths,phy,che]
    db.execute("insert into student values(?,?,?,?,?)",list1)
    db.commit()
    print("----------------------------------------------------------")

def checkPercentage():
    cursor = db.cursor()
    
    roll = int(input("Enter RollNumber:"))
    while roll < 1:
        print("Invalid Value! please enter roll number above 1")
        roll = int(input("Enter RollNumber:"))

    cursor.execute("select * from student where roll = ?",[roll])
    list1 = cursor.fetchall()[0]
    perc = (list1[2] + list1[3] + list1[4])/3
    print("Student Percentage is: %.2f"%perc)
    print("Student Roll Number:",list1[0])
    print("Student Name:",list1[1])
    print("Maths Marks:",list1[2])
    print("Physics Marks:",list1[3])
    print("Chemistry Marks:",list1[4])
    
    print(list1)
    print("----------------------------------------------------------")

def generateReport():
    f = open("student_db.csv","w",newline="")
    obj = csv.writer(f)

    cursor = db.cursor()
    cursor.execute("select * from student")
    list1 = cursor.fetchall()
    
    for tuple1 in list1:
        perc = int((tuple1[2] + tuple1[3] + tuple1[4])/3)

        status = "fail"
        if perc >= 40:
            status = "pass"

        list2 = list(tuple1)    
        list2.append(int(perc))
        list2.append(status)
        obj.writerow(list2)

    cursor.close()
    f.close()
    print("Report Generated into csv file successfully!")
    print("----------------------------------------------------------")

def sendReport():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    
    usr = input("Enter username:")
    p = getpass.getpass(prompt="Enter your password:")
    server.login(usr,p)

    receiver = input("Enter receiver's email id:")
    msg = str("This is mail from nandhakumar")
    server.sendmail(usr,receiver,msg)
    print("----------------------------------------------------------")

while True:
    print("----------------------------------------------------------")
    print("Enter one choice:\n1. Add Data\n2. Check Percentage\n3. Generate Report\n4. Send Report\n5. Exit")
    ch = int(input("Choice:"))
    print("----------------------------------------------------------")

    if ch == 1:
        addData()
    elif ch == 2:
        checkPercentage()
    elif ch == 3:
        generateReport()
    elif ch == 4:
        sendReport()
    elif ch == 5:
        print("Thanks for contacting! bye!")
        db.close()
        break
    else:
        print("Invalid choice!")
        
