# if - else
#Example 1
##num = int(input("Enter a number:"))
##
##if num%2 == 0:
##    print("even")
##else:
##    print("odd")

# Example 2

# vowel or consonant
# nested if else
# if char == "a" or char == "e" or char =="i" -> not using it

##char = input("Enter a char:")
##
##if char.isalpha() and len(char) == 1:
##    if char in "aeiouAEIOU":
##        print("Its a vowel")
##    else:
##        print("Its a consonant")
##else:
##    print("Invalid input")
##    

# Example 3

##a = float(input("Enter a length of side A:"))
##b = float(input("Enter a length of side B:"))
##c = float(input("Enter a length of side C:"))
##
##if a == b and b == c:
##    print("equilateral traingle")
##elif a == b or b == c or a == c:
##    print("isosceles triangle")
##else:
##    print("scalene triangle")

# Example 4

##str1 = input("Enter a string of number:")
##
##num = len(str1)
##
##if str1[num-1].isnumeric() and str1[num-2].isnumeric() and str1[num-3].isnumeric():
##    sum1 = int(str1[num-1]) + int(str1[num-2]) + int(str1[num-3])
##    print("It's a valid string! Last 3 digits are ",str1[num-3],str1[num-2],str1[num-1])
##    print("The sum of last 3 digit number is:",sum1)
##else:
##    print("It's a Invalid string!")
