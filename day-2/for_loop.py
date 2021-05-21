# For loop in python

# Example-1:

##list1 = [10,20,30,40,50]
##
##for item in list1:
##    print(item*5)
##
##print("bye")

# Example-2:
'''
list1 = [10,20,30,40,50]
list2 = []

for item in list1:
    list2.append(item*5)

print(list2)
'''

# Example-3:
'''
list1 = [10,20,30,40,50]
list2 = []

for item in list1[2:]:
    list2.append(item*5)

print(list2)
'''

# Example-4:

##list1 = [1,2,3,4,5,6,7,8,9,10]
##even = []
##odd = []
##
##for i in list1:
##    if i%2 == 0:
##        even.append(i)
##    else:
##        odd.append(i)
##
##print(even)
##print(odd)

# Example -5:
# range (start,stop,step)

#1
'''
for i in range(10):
    print(i)
'''

#2
'''
for i in range(100,110):
    print(i)
'''

#3
'''
for i in range(100,110,2):
    print(i)
'''

#4
'''
for i in range(110,100,-1):
    print(i)
'''

#Example -6:  range
'''
list1 = []
for i in range(1000,1500):
    if i%7 == 0:
        list1.append(i)

print(list1)
print("Total Elements",len(list1))
'''

# For loop with string data type

#example -1
'''
str1 = input("Enter a string:")
v = []
c = []

for i in str1:
    if i in "aeiouAEIOU":
        v.append(i)
    elif i == " ":
        pass # skip / do nothing
    else:
        c.append(i)

print(v,"Total Vowels:",len(v))
print(c,"Total Consonants:",len(c))
'''

# example - 2

'''
str1 = input("Enter a string:")

num = []
alpha = []
garbage = []

for i in str1:
    if i.isalpha():
        alpha.append(i)
    elif i.isnumeric():
        num.append(i)
    else:
        garbage.append(i)

print(alpha)
print(num)
print(garbage)
'''

# example -3 
'''
sub = int(input("Enter number of subjects:"))
list1 = []
for item in range(1,sub+1):
    marks = int(input("Enter Marks in sub %i:"%item))
    list1.append(marks)

print(list1)
perc = sum(list1)/sub
print("Percentage: %.2f"%perc)
'''

# example -4

'''
num = int(input("Enter number of elements:"))
list1 = []
for item in range(1,num+1):
    list1.append(int(input("Enter Element:")))

list1.sort()
print("Second largest elements is:",list1[-2])
'''

# ex -5

'''
num1 = int(input("Enter number of elements for list 1:"))
list1 = []
for item in range(1,num1+1):
    list1.append(int(input("Enter element:")))
    
num2 = int(input("Enter number of elements for list 1:"))
list2 = []
for item in range(1,num2+1):
    list2.append(int(input("Enter element:")))

list1.extend(list2)
list1.sort()
print("Sorted list is:",list1)
'''

# ex -6
'''
num1 = int(input("Enter the low range:"))
num2 = int(input("Enter the upper range:"))

list1 =[]

for item in range(num1,num2+1) :
    list1.append((item,item**2))

print(list1)
'''

# ex - 7
'''
list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]
list3 = []

for i in range(len(list1))
    list3.append(list1[])

'''

# ex -8
'''
list1 = ["aman","gopal","yash","ankita"]

list2 = []

for i in list1:
    if i[0] in "aeiouAEIOU":
        list2.append(i)

print(list2)
'''

# ex -9
'''
list1 = [10,20,30,10,20,30]
final_list = []

for i in list1:
    if i not in final_list:
        final_list.append(i)
print(final_list)
'''

# ex-10
'''
str1 = input("Enter a String")
upper = []
lower = []

for i in str1:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
'''

# ex -11

'''
list1 = ["abc@gmail.com","cde@yahoo.com","fgh@oracle.com"]

gmail = []
yahoo = []
oracle = []

for i in list1:
    if i.endswith("@gmail.com"):
        gmail.append(i)
    elif i.endswith("@yahoo.com"):
        yahoo.append(i)
    elif i.endswith("@oracle.com"):
        oracle.append(i)
    else:
       pass
    
print(gmail)
print(yahoo)
print(oracle)
'''

# ex -12

list1 = [10,25,36,84,92]
list2 = []

for i in list1:
    list2.append(int(i/10))

print(sum(list2))
