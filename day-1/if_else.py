# Conditional Programming in Python
# if - else

# Example-1:

'''
marks = int( input("Enter your marks:"))

if marks<35:
    print("Fail")
    print("Study hard for the next year")
else:
    print("Pass")
    print("Let's Celebrate!!")
'''

# Example-2:

"""
marks = int( input("Enter your marks:"))

if marks<35:
    print("Grade D")
elif marks>=35 and marks<50:
    print("Grade C")
elif marks>=50 and marks<75:
    print("Grade B")
elif marks>=75 and marks<=100:
    print("Grade A")
else:
    print("Invalid Marks!")
"""

# Example-3:
'''
num1 = int( input("Enter num1:"))
num2 = int( input("Enter num2:"))

if num2>num1:
    print("num2 is bigger")
elif num1>num2:
    print("num1 is bigger")
elif num1 == num2:
    print("They are equal")

'''

# Example -4:

'''
phno = input("Enter your phone number:")

if phno.isnumeric() and len(phno) == 10:
    print("Valid number")
else:
    print("Invalid number")
'''

# Example -5
'''
name = input("Enter your name:")

if name.isalpha():
    print("Valid name")
else:
    print("Invalid name")
'''

# Example -6

'''
str1 = input("Enter string 1:")
str2 = input("Enter string 2:")

if len(str1) < len(str2):
    print("Length of %s is smaller than %s"%(str1,str2))
else:
    print("Length of %s is smaller than %s"%(str2,str1))
'''

# Example -7
'''
str1 = input("Enter string: ")
str2 = input("Enter word:")

if str1.find(str2) != -1:
    print("Substring found in string")
else:
    print("Substing not found in string")
    '''

# Example - 8

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meter:"))

BMI = weight/(height*height)

if BMI >= 27.5:
    print("High Risk")
elif BMI >=23:
    print("Moderate Risk")
elif BMI >=18.5:
    print("Low Risk")
else
    print("Risk of nutritional deficiency diseases")

