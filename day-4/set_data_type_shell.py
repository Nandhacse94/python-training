Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Set data type in python
>>> set1 = {10,20,30,40,50}
>>> type(set1)
<class 'set'>
>>> 
>>> set2 = {10,20,30,10,20,30,40,50,30,20,40}
>>> set2
{50, 20, 40, 10, 30}
>>> 
>>> # Duplicate elements are not allowed
>>> # No indexing
>>> # No fix order of elements
>>> # No accessing of elements
>>> set2[2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set2[2]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> # set itself is mutable
>>> # there elements are immutable
>>> 
>>> set1[2] = 200
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set1[2] = 200
TypeError: 'set' object does not support item assignment
>>> 
>>> 
>>> set1
{50, 20, 40, 10, 30}
>>> set1.add(60)
>>> set1
{50, 20, 40, 10, 60, 30}
>>> 
>>> 
>>> # add()
>>> # remove() - error will be thrown, when element is not available in set
>>> # discard() - no err will be thrown, even element is not available in set
>>> 
>>> set1
{50, 20, 40, 10, 60, 30}
>>> set1.remove(50)
>>> set1.remove()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    set1.remove()
TypeError: set.remove() takes exactly one argument (0 given)
>>> set1
{20, 40, 10, 60, 30}
>>> set1.remove(50)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    set1.remove(50)
KeyError: 50
>>> 
>>> set1
{20, 40, 10, 60, 30}
>>> set1.discard(60)
>>> set1
{20, 40, 10, 30}
>>> set1.discard(60)
>>> 
>>> 
>>> 
>>> a = {1,2,3,4,5}
>>> b = {4,5,6,7,8}
>>> 
>>> # union
>>> # set of all the elements from both set
>>> 
>>> a|b
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> 
>>> 
>>> # insersection
>>> # set of common elements in both set
>>> 
>>> a&b
{4, 5}
>>> 
>>> a.intersection(b)
{4, 5}
>>> b.intersection(a)
{4, 5}
>>> 
>>> 
>>> # difference
>>> # only uncommon elements
>>> 
>>> a-b
{1, 2, 3}
>>> b-a
{8, 6, 7}
>>> 
>>> a.difference(b)
{1, 2, 3}
>>> 
>>> b.difference(a)
{8, 6, 7}
>>> b.difference(a)
{8, 6, 7}
>>> 
>>> 
>>> # symmetric difference
>>> 
>>> # except the common elements
>>> 
>>> a^b
{1, 2, 3, 6, 7, 8}
>>> 
>>> b^a
{1, 2, 3, 6, 7, 8}
>>> 
>>> a.symmetric_difference(b)
{1, 2, 3, 6, 7, 8}
>>> b.symmetric_difference(a)
{1, 2, 3, 6, 7, 8}
>>> 
>>> 
>>> # subset and superset
>>> # child and parent kind of thing
>>> 
>>> a = {1,2,3,4,5,6,7}
>>> b = {2,5,7}
>>> 
>>> b.issubset(a)
True
>>> a.superset(b)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'
>>> a.issuperset(b)
True
>>> 
>>> b.issuperset(a)
False
>>> a.issubset(b)
False
>>> 
>>> 
>>> 
>>> 
>>> # set data type
>>> # add() remove() discard()
>>> # union() -> symbol used -> |
>>> # intersection() -> symbol used -> &
>>> # difference() -> symbol used -> -
>>> # symmetric_difference() -> symbol used -> ^
>>> #
>>> # issubset()
>>> # issuperset()
>>> 