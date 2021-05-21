# Dictionary Examples

# eg 1:
# range of 10 elements with square
'''
squares = {}

for i in range(1,11):
    squares[i] = i*i

print(squares)
'''

# eg 2:

'''
even = {}
odd = {}
for i in range(1,11):
    if i%2 == 0:
        even[i] = i*i
    else:
        odd[i] = i*i*i

print(even)
print(odd)
'''

# eg 3:

# student db mgmt
# dict datatype
'''
data = {}

def addStudent():
    print("---- ADD A NEW STUDENT HERE ----")
    name = input("Enter your name:")
    if name.isalpha() == False:
        print("Invalid name! Please try again")
        name = input("Enter your name:")
    if data.get(name):
        print("Student Name %s already exists!"%name.upper())
        return
    s1 = float(input("Enter your English Mark:"))
    s2 = float(input("Enter your Maths Mark:"))
    s3 = float(input("Enter your Science Mark:"))
    data[name] = [s1,s2,s3]
    print("Entry for Student %s has added successfully:"%(name.upper()),data[name])

def calcPerc():
    print("---- CALCULATE PERCENTAGE HERE ----")
    name = input("Enter your name to calculate percentage:")
    if name.isalpha() == False:
        print("Invalid name! Please try again")
        name = input("Enter your name:")
    perc = (data[name][0] + data[name][1] + data[name][2])/3
    print("Percentage of %s is %i"%(name,perc))
    
while True:
    print("1. Add student")
    print("2. Calculate percentage")
    print("3. Exit")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        addStudent()
    elif ch == 2:
        calcPerc()
    elif ch == 3:
        print("Bye")
        break
    else:
        print("Invalid Choice")

'''

