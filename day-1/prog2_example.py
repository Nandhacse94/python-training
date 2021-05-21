# Example 2

##print("**** Student Data Base ****")
##fname = input("Enter First name:")
##lname = input("Enter Last name:")
##phone = input("Enter phone number:")
##marks = input("Enter marks:")
##
##print("---- Student Data Received ----")
##print("Name:",fname,lname)
##print("Phone number: %s",%phone)
##print("Marks: {}".format(phone))

# Example 3

##num1 = int(input ("Enter number 1:"))
##num2 = int(input ("Enter number 2:"))
##
##print("Addition",num1+num2)
##print("Subtraction %i "%(num1-num2))
##print("Multiplication {}".format(num1*num2))
##print("Division %i "%(num1/num2))
##


# Example 4

s1 = int( input("Enter marks in Sub1:") )
s2 = int( input("Enter marks in Sub2:") )
s3 = int( input("Enter marks in Sub3:") )
s4 = int( input("Enter marks in Sub4:") )
s5 = int( input("Enter marks in Sub5:") )

perc = (s1+s2+s3+s4+s5)/5

print("Percentage:",perc)
print("Percentage: %.2f"%perc)
print("Percentage: {}".format(perc))


print("Highest Marks:",max(s1,s2,s3,s4,s5))
print("Lowest Marks:",min(s1,s2,s3,s4,s5))
