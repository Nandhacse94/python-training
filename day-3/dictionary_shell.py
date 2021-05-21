Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Dictionary data type
>>> # use {} to create dict and key:value pair
>>> 
>>> dict1 = {"apple":"red","banana":"yellow"}
>>> len(dict1)
2
>>> type(dict1)
<class 'dict'>
>>> 
>>> # Accessing data from the dictionary
>>> # no indexing
>>> # we use keys to access the data
>>> 
>>> dict1["apple"]
'red'
>>> dict1["red"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    dict1["red"]
KeyError: 'red'
>>> dict1["banana"]
'yellow'
>>> 
>>> # get()
>>> dict1.get("apple")
'red'
>>> # check for value with first paramter
>>> # if found, return value or nothing
>>> # so if you pass second parameter, instead of nothing, it will print second param
>>> # incase if first param not found
>>> 
>>> dict.get("apple","not found")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict.get("apple","not found")
TypeError: descriptor 'get' for 'dict' objects doesn't apply to a 'str' object
>>> dict1.get("apple","not found")
'red'
>>> dict1.get("guava","not found")
'not found'
>>> 
>>> 
>>> # No indexing
>>> # No fix order of elements
>>> # Duplicate keys are not allowed
>>> # Duplicate values are allowed
>>> 
>>> # keys -> immutable data type
>>> # values -> any data type
>>> 
>>> # Dictionary is a mutable data type
>>> 
>>> dict1 = {"name":"sam","age":25}
>>> dict1["age"] = 26
>>> dict1
{'name': 'sam', 'age': 26}
>>> dict1["address"] = "bangalore"
>>> dict1
{'name': 'sam', 'age': 26, 'address': 'bangalore'}
>>> dict1["phone"] = 99876
>>> dict1
{'name': 'sam', 'age': 26, 'address': 'bangalore', 'phone': 99876}
>>> 
>>> # update() :- add one dictionary to another dictionary
>>> 
>>> dict2 = {"ID":"PAN CARD"}
>>> dict1.update(dict2)
>>> dict2["ID"] = "PAN01234"
>>> dict1.update(dict2)
>>> dict1
{'name': 'sam', 'age': 26, 'address': 'bangalore', 'phone': 99876, 'ID': 'PAN01234'}
>>> # keys() and values()
>>> dict1.keys()
dict_keys(['name', 'age', 'address', 'phone', 'ID'])
>>> 
>>> dict1.values()
dict_values(['sam', 26, 'bangalore', 99876, 'PAN01234'])
>>> 
>>> # pop()
>>> dict1.pop("age")
26
>>> del dict1["address"]
>>> dict1
{'name': 'sam', 'phone': 99876, 'ID': 'PAN01234'}
>>> 
>>> # clear()
>>> 
>>> dict1
{'name': 'sam', 'phone': 99876, 'ID': 'PAN01234'}
>>> dict1.clear()
>>> dict1
{}
>>> del dict1
>>> dict1
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    dict1
NameError: name 'dict1' is not defined
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> keyword.kwlist()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    keyword.kwlist()
TypeError: 'list' object is not callable
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> 
>>> 
>>> # zip()
>>> 
>>> list1 = ["name","age","address"]
>>> list2 = ["sam",12,"delhi"]
>>> 
>>> dict(zip(list1,list2))
{'name': 'sam', 'age': 12, 'address': 'delhi'}
>>> 
>>> list(zip(list1,list2))
[('name', 'sam'), ('age', 12), ('address', 'delhi')]
>>> 
>>> tuple(zip(list1,list2))
(('name', 'sam'), ('age', 12), ('address', 'delhi'))
>>> 
>>> 
>>> 
>>> # access list as values in dict
>>> dict1 = {"even":[2,4,6],"odd":(1,3,5)}
>>> type(dict1["even"])
<class 'list'>
>>> type(dict1["odd"])
<class 'tuple'>
>>> dict1["even"].append(8)
>>> dict
<class 'dict'>
>>> dict1
{'even': [2, 4, 6, 8], 'odd': (1, 3, 5)}
>>> dict1["odd"]
(1, 3, 5)
>>> dict1["even"][0]
2
>>> dict1["odd"][0]
1
>>> 
>>> dict1 = {101:{"name":"sam","salary":25000},102:{"name":"john","salary":20000}
	 }
>>> dict1
{101: {'name': 'sam', 'salary': 25000}, 102: {'name': 'john', 'salary': 20000}}
>>> dict1[101]
{'name': 'sam', 'salary': 25000}
>>> dict1[101]["salary"]
25000
>>> type(dict1[101])
<class 'dict'>
>>> dict1[101]["salary"] = 30000
>>> dict1[101]["salary"]
30000
>>> 
>>> 
>>> 
>>> 
>>> # dict
>>> # key : value
>>> # get()
>>> # get(key,"not found err msg")
>>> # no index, unordered
>>> # duplicate keys not allowed
>>> # duplicate values allowed
>>> 
>>> # dictionary is mutable data type
>>> # update()
>>> # keys()
>>> # values()
>>> # pop()
>>> # del
>>> # clear()
>>> # zip
>>> # append()
>>> 