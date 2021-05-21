# List Comprehension

# eg 1

'''
list1 = [10,20,30,40,50]
list2 = []

for i in list1:
    list2.append(i*5)

print(list2)
'''

# eg 2
'''
list1 = [10,20,30,40,50]
list2 = [i*5 for i in list1]
print(list2)
'''

# eg 3

even = [i for i in range(1,11) if i%2 == 0]
odd = [i for i in range(1,11) if i%2 != 0]

print(even)
print(odd)
