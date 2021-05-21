a = 10

# to take input from user in cli window.
# it will take input by default as string
# we can pass string to show in cli - input("Enter the value of b:")
# we have to typecast the string to integer like int(input())
b = int( input("Enter the value of b:") )

c = a + b

print("The sum of a and b is : ", c) 

# Ways of writing print function:
## Part 1:

# format identifiers is not must needed.
# print func can take 'n' number of arguments.
print("The sum of ",a," and ",b," is :",c)

# commenting the line - shortcut is alt +3
# uncommenting the line - shortcut is alt + 4

## Part 2:

print("The sum of %i and %i is %i"%(a,b,c))

# %i -> int
# %f -> float
# %s -> string

## Part 3:
print("The sum of {} and {} is {}".format(a,b,c))
