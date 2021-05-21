# python with SQL database

import sqlite3

# create a db
db = sqlite3.connect("DB1.sqlite")

# create a table with column

try:
    db.execute("create table student(name text, address text, phone text)")
except:
    pass

# Insert rows
# db.execute("insert into student values('sam','delhi','998877')") # method 1
# db.execute("insert into student values('john','pune','996655')")

list1 = []
list1.append(input("Enter name:"))
list1.append(input("Enter phone:"))
list1.append(input("Enter address:"))

db.execute("insert into student values(?,?,?)",list1) # method 2 # pass input at runtime

db.commit() # save the data

# Extracting data from the database
cursor = db.cursor()

# cursor.execute("select * from student") # method 1

name = input("Enter the name to extract the data:")
cursor.execute("select * from student where name = ?",[name]) # method 2 # pass input at runtime

list1 = cursor.fetchall()
print( list1 )

cursor.close()
db.close()


# db = sqlite3.connect("filename.sqlite")
#
# db.execute("insert into table values")
#
# db.commit()
#
# cursor = db.cursor()
#
# list1 = cursor.fetchall()
# list of tuples # each tuple is each row

# cursor.close()
# db.close()
