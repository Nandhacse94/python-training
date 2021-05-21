# Exception Handling in python

# try
# except
'''
try:
    n1 = int(input("Enter num1: ")) # ValueError: if value is not int
    n2 = int(input("Enter num2: "))
    result = n1/n2 # Possibilty of ZeroDivisionError

    print(result)

except ZeroDivisionError:
    print("You can not divide a number by zero")
    
except ValueError:
    print("Invalid Input")
'''
# finally
'''
try:
    n1 = int(input("Enter num1: ")) # ValueError: if value is not int
    n2 = int(input("Enter num2: "))
    result = n1/n2 # Possibilty of ZeroDivisionError

    print(result)
except:
    print("Invalid value")
finally:
    print("Bye!")
'''

# User defined Exception
# Guess the number game

import random

class SmallError(Exception):
    pass

class LargeError(Exception):
    pass

class Success(Exception):
    pass

def randomUser(list1):
    usr = random.choice(list1)
    return usr

# initial inputs from the Players
print("*---------GUESS THE NUMBER------------*")
print("Press '1' to start game\nPress '2' to exit")
ch = int(input("Enter choice:"))
playcount = int(input("Enter number of players:"))
playerlist = []

for i in range(0,playcount):
    playerlist.append(input("Enter player name:"))
    
start = int(input("Enter start value:"))
stop = int(input("Enter stop value:"))
print("Picking 1 random number between %i and %i\n . . . . . . . Done!!"%(start,stop))
number = random.randint(start,stop)
tries = [0,0,0]

while True:

    print("------------------------------------------------------")
    player = randomUser(playerlist)
    num = int(input("Hey !! %s \nGuess the Number:::"%player))
    tries[playerlist.index(player)] += 1;
    
    try:
        if num < number:
            raise SmallError
        elif num>number:
            raise LargeError
        else:
            raise Success
    except SmallError:
        print("Your number is SMALL !! Please guess the Bigger Number")

    except LargeError:
        print("Your number is BIG !! Please guess the Smaller Number")

    except Success:
        print("Congratulations!! %s Won the game"%player)
        print("The Correct Number is ",num)
        print("Total attempts:",tries[playerlist.index(player)])
        print("------------------------------------------------------")
        break


