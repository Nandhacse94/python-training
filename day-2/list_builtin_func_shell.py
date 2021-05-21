Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # List Built-in functions
>>> 
>>> #append()
>>> # it will add an element at the end of your list
>>> 
>>> list1 = [10,20,30]
>>> list1.append(40)
>>> list1
[10, 20, 30, 40]
>>> list1.append("python")
>>> list1
[10, 20, 30, 40, 'python']
>>> 
>>> # insert()
>>> # index_num, element
>>> 
>>> list1.insert(2,"cat")
>>> list1
[10, 20, 'cat', 30, 40, 'python']
>>> # it will add the "cat" element in index pos 2 and move the existing elements to right
>>> 
>>> # extend()
>>> list1
[10, 20, 'cat', 30, 40, 'python']
>>> list2 = [100,200]
>>> list1 = extend(list2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list1 = extend(list2)
NameError: name 'extend' is not defined
>>> list1.extend(list2)
>>> list1
[10, 20, 'cat', 30, 40, 'python', 100, 200]
>>> # it will append the argument list in end of the list1
>>> 
>>> # list3 = list1 + list2
>>> 
>>> # remove()
>>> # based on the element
>>> list1
[10, 20, 'cat', 30, 40, 'python', 100, 200]
>>> list1.remove("python")
>>> list1
[10, 20, 'cat', 30, 40, 100, 200]
>>> list1.remove("python")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list1.remove("python")
ValueError: list.remove(x): x not in list
>>> list1[2:3] = ["python","python","python"]
>>> list1
[10, 20, 'python', 'python', 'python', 30, 40, 100, 200]
>>> list1.remove("python")
>>> list1
[10, 20, 'python', 'python', 30, 40, 100, 200]
>>> # so it will remove only first occurence of python
>>> 
>>> # pop()
>>> 
>>> # based on the index number
>>> list1
[10, 20, 'python', 'python', 30, 40, 100, 200]
>>> list1.pop(2)
'python'
>>> list1
[10, 20, 'python', 30, 40, 100, 200]
>>> list1.pop()
200
>>> list1
[10, 20, 'python', 30, 40, 100]
>>> # by default pop func will delete end of the element
>>> 
>>> # clear()
>>> list1
[10, 20, 'python', 30, 40, 100]
>>> list1.clear()
>>> list1
[]
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> # clear will only clear the value, delete will delete the variable itself
>>> a =10
>>> del 1
SyntaxError: cannot delete literal
>>> del a
>>> del a
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    del a
NameError: name 'a' is not defined
>>> list1 = [10,20,30,40,50]
>>> list1
[10, 20, 30, 40, 50]
>>> del list1[2]
>>> list1
[10, 20, 40, 50]
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> 
>>> 
>>> list1 = [10,20,30,40,50]
>>> len(list1)
5
>>> max(list1)
50
>>> min(list1)
10
>>> sum(list1)
150
>>> 
>>> # count()
>>> 
>>> list1 = [10,20,30,10,20,10]
>>> list1.count(10)
3
>>> list1.count(20)
2
>>> list1.count(30)
1
>>> 
>>> 
>>> # sort() and reverse()
>>> list1 = [20,10,90,80,30]
>>> list1.sort()
>>> list1
[10, 20, 30, 80, 90]
>>> list1.reverse()
>>> list1
[90, 80, 30, 20, 10]
>>> list1.index(30)
2
>>> 
>>> 
>>> # functions()
>>> # append()
>>> # insert()
>>> # extend()
>>> # remove()
>>> # pop()
>>> # clear()
>>> # del
>>> # count()
>>> # max(), min(), sum()
>>> # sort()
>>> # reverse()
>>> 