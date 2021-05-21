# Example 1
# using 3 types of inputs in print func 
# inventor of python
# guido van rossum

fname = input("Enter your First name:")
mname = input("Enter your Middle name:")
lname = input("Enter your Last name:")

print("Good Morning!!",fname,mname,lname)

print("Good Morning!! %s %s %s"%(fname,mname,lname))

print("Good Morning!! {} {} {}".format(fname,mname,lname))

#Output

##Enter your First name:guido
##Enter your Middle name:van
##Enter your Last name:rossum
##Good Morning!! guido van rossum
##Good Morning!! guido van rossum
##Good Morning!! guido van rossum

#if you want to print without spaces.

# wname = fname + mname + lname
