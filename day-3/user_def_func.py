#user defined function

# example-1
'''
def func():
    print("This is my func()")

func() # function call
'''

# example 2
'''
def func(text):
    print(text)

func("hello world")
func("hello python")
'''

# example 3
# parameterized function and function return

'''
def addNum(x,y):
    result = x+y
    return result,x,y,"hello python"    # return as tuple

def subNum(x,y):
    result = x-y
    return result 

while True:
    print("1. Add")
    print("2. Sub")
    print("4.exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        n1 = int(input("Enter num1:"))
        n2 = int(input("Enter num2:"))
        print(addNum(n1,n2))
        
    elif ch == 2:
        n1 = int(input("Enter num1:"))
        n2 = int(input("Enter num2:"))
        var = subNum(n1,n2)
        print(var)

    elif ch == 4:
        break

    else:
        print("Invalid choice")    

'''

# Default Values

'''
def func(x=0,y=0):
    print(x)
    print(y)

func()
func(100,200)
func(20)
'''

# *args
# args will take input as tuples

def func(x,y,*args):
    print(x)
    print(y)
    print(args)

func(10,20)
func(10,20,"hello python",50)
