Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Comparison operator or relational operator
>>> 
>>> a = 10
>>> b = 20
>>> c = 10
>>> a == b
False
>>> a == c
True
>>> a > b
False
>>> 
>>> a < b
True
>>> a >= b
False
>>> a <= b
True
>>> a != b
True
>>> # Membership operator
>>> # in and not in
>>> str1 = "this is python training"
>>> "python" in str1
True
>>> "Python" in str1
False
>>> "cat" in str1
False
>>> "cat" not in str1
True
>>> "python" not in str1
False
>>> 
>>> 
>>> 
>>> list1 = [10,20,30,40,50]
>>> 100 in list1
False
>>> 100 not in list1
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #string data type in python
>>> str1 = "python"
>>> #Accessing elements from the string
>>> # Index number
>>> str1[2]
't'
>>> str1[0]
'p'
>>> str1[-1]
'n'
>>> str1[-4]
't'
>>> # Multiple elements
>>> # : -> slicing operator
>>> 
>>> str1[1:4]
'yth'
>>> str1[1:]
'ython'
>>> str1[:4]
'pyth'
>>> str1[:]
'python'
>>> 
>>> # [start:stop:step]
>>> # step -> 1
>>> 
>>> str1[1:4:1]
'yth'
>>> # to read in reverse direction
>>> str1[4:1:-1]
'oht'
>>> str1[::-1]
'nohtyp'
>>> 
>>> # to skip elements in between in the string / print alternate chars
>>> str1[::2]
'pto'
>>> str1[::-2]
'nhy'
>>> str1[::3]
'ph'
>>> str1[4:-5:-2]
'ot'
>>> str1[-4:-2:-1]
''
>>> str1[-2::-1]
'ohtyp'
>>> 