Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hello world
SyntaxError: invalid syntax
>>> print("hello world")
hello world
>>> # variables in python
>>> 
>>> a = 10
>>> type(a)
<class 'int'>
>>> 
>>> b = 2.5
>>> type(b)
<class 'float'>
>>> 
>>> c = "Hello"
>>> type(c)
<class 'str'>
>>> 
>>> 
>>> 
>>> 
================================ RESTART: Shell ================================
>>> 
>>> # Rules of writing variable names in python
>>> 
>>> #1 - Start -> a-z or A-Z or _
>>> #2 - Not start -> 0-9
>>> 
>>> abc = 10
>>> Abc = 10
>>> _ab = 10
>>> 
>>> lab = 10
>>> 2ab = 10
SyntaxError: invalid syntax
>>> 
>>> #3 - Spaces are not allowed
>>> abc =10
>>> a bc = 10
SyntaxError: invalid syntax
>>> 
>>> #4 - Keywords are not allowed
>>> # Python is case sensitive
>>> true = 10
>>> True = 10
SyntaxError: cannot assign to True
>>>
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> 
>>> 
>>> 
>>> # Arithmetic Operators
>>> 5 + 2
7
>>> 5 - 2
3
>>> 5 * 2
10
>>> 5 / 2
2.5
>>> 5 % 2
1
>>> 5 // 2
2
>>> # // -> floor division
>>> 
>>> 2 ** 5
32
>>> # ** -> exponent
>>> 
>>> # Strings in python
>>> a = "python"
>>> type(a)
<class 'str'>
>>> 
>>> b = 'hello'
>>> type(b)
<class 'str'>
>>> 
>>> # Arithmetic operators used in python are + and *
>>> b+a
'hellopython'
>>> 
>>> a*5
'pythonpythonpythonpythonpython'
>>> 
>>> b*2
'hellohello'
>>> 
