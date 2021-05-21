# While Loop

# prog 1
'''
n = 1
while n<=10:
    print(n)
    n = n+1
'''

# prog 2

# menu driven program
# simple calc example

# indent -> CTRL + ]
# unindent -> CTRL + [

'''
while True:
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

    ch = int( input("Enter your choice:"))

    if ch == 1:
        n1 = int(input("Enter num 1:"))
        n2 = int(input("Enter num 2:"))
        print("Addition:",n1+n2)
    elif ch == 2:
        n1 = int(input("Enter num 1:"))
        n2 = int(input("Enter num 2:"))
        print("Subtraction:",n1-n2)
    elif ch == 3:
        n1 = int(input("Enter num 1:"))
        n2 = int(input("Enter num 2:"))
        print("Subtraction:",n1*n2)
    elif ch == 4:
        break # to exit from the loops
    else:
        print("Invalid choice")
    
'''



# prog 3

while True:

    print("1. Binary")
    print("2. Octal")
    print("3. Hexa")
    print("4. Exit")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        num = int(input("Enter a number to convert:"))
        print(format(num,'b'))
    elif ch == 2:
        num = int(input("Enter a number to convert:"))
        print(format(num,'o'))
    elif ch == 3:
        num = int(input("Enter a number to convert:"))
        print(format(num,'x'))
    elif ch == 4:
        break
    else:
        print("Invalid choice!!")

    
