Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # String Built in Functions
>>> # capitalize()
>>> 
>>> str1 = "pyTHoN"
>>> str1.capitalize()
'Python'
>>> str1
'pyTHoN'
>>> 
>>> # string is an immutable data type
>>> 
>>> str2 = str1.capitalize()
>>> str2
'Python'
>>> str1
'pyTHoN'
>>> # lower() and upper()
>>> 
>>> str1
'pyTHoN'
>>> str1.lower()
'python'
>>> str1.upper()
'PYTHON'
>>> str1
'pyTHoN'
>>> 
>>> # swapcase()
>>> str1.swapcase()
'PYthOn'
>>> str1
'pyTHoN'
>>> # title()
>>> 
>>> str1.title()
'Python'
>>> # count()
>>> str1.count()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    str1.count()
TypeError: count() takes at least 1 argument (0 given)
>>> str1 = "i play cricket and i play chess"
>>> str1.count("play")
2
>>> str1.count("i")
3
>>> str1.count("i ")
2
>>> str1.count("J")
0
>>> # islower() and isupper()
>>> str1 = "python"
>>> str1.islower()
True
>>> str1.isupper()
False
>>> str1 = "pYthon"
>>> str1.lower()
'python'
>>> str1.islower()
False
>>> str1.isupper()
False
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> # isdecimal() and isalpha() - to check values is decimal or alpha
>>> str1 = "3535635787"
>>> str1.isdecimal()
True
>>> str1 = "25435fdvdfsgfd23423"
>>> str1.isdecimal()
False
>>> str1.isalpha()
False
>>> str1 = "python"
>>> str1.isalpha()
True
>>> 
>>> # isdigit() or isnumeric()
>>> 
>>> # isalnum()
>>> # alphabets or number or both
>>> 
>>> str1 = "abc123"
>>> str1.isalnum()
True
>>> str1.isdigit()
False
>>> str1 = "123-*abc"
>>> str1.isalnum()
False
>>> str1 = "12345"
>>> str1.isdigit()
True
>>> str1.isnumeric()
True
>>> # find() and index()
>>> 
>>> str1 = "this is python training"
>>> 
>>> "python" in str1
True
>>> str1.find("python")
8
>>> str1.find("cat")
-1
>>> str1.index("python")
8
>>> str1.index("cat")
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    str1.index("cat")
ValueError: substring not found
>>> str1 = "hello python and learn python"
>>> str1.find("python")
6
>>> str1.find("python",7)
23
>>> # it looks for python keyword from the 7th index
>>> str1.find("python",7,21)
-1
>>> # it looks for python keyword between 7th and 21 index
>>> 
>>> #replace()
>>> str1 = "hello john and hello michael"
>>> str1.replace("hello","hi")
'hi john and hi michael'
>>> 
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> # split()
>>> # will return a list of substring
>>> 
>>> str1 = "hello how are you"
>>> str1.split()
['hello', 'how', 'are', 'you']
>>> str1.split().len()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    str1.split().len()
AttributeError: 'list' object has no attribute 'len'
>>> list1 = str1.split()
>>> list1
['hello', 'how', 'are', 'you']
>>> len(list1)
4
>>> str1 = "abcdef"
>>> len(str1)
6
>>> str1 = "hello how*are you"
>>> str1.split("*")
['hello how', 'are you']
>>> # delimiters - by default split() will take space as argument or else we can pause any char/string as delimiter
>>> 
>>> # strip(), rstrip() and lstrip()
>>> str1.strip()
'hello how*are you'
>>> str1 = "         python         "
>>> str1
'         python         '
>>> str1.strip()
'python'
>>> str1.rstrip()
'         python'
>>> str1.lstrip()
'python         '
>>> str1 = "******python-------"
>>> str1.strip(*)
SyntaxError: invalid syntax
>>> str1.strip("*")
'python-------'

>>> str1.rstrip("-")
'******python'
>>> str1.lstrip("*")
'python-------'
>>> 
