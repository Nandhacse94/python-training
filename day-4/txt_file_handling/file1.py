# txt file handling

'''
1) open a file
2) read/write
3) close the file

open(filename,mode)

mode -> r (read), w(write), a(append)
'''

# eg1
'''
f = open("source.txt","r") #1

print(f.read()) #2

f.close() #3
'''

# eg2
# readline()
'''
f = open("source.txt") # by default it will open the file in read mode

print(f.readline())
print(f.readline())

f.close()
'''

# eg3
# readlines()
# it will return a list of each line
'''
f = open("source.txt")
#print(f.readlines())
list1 = f.readlines() 
print(list1)
f.close()
'''


# writing data into txt file
# w(write) and a(append)
# w and a -> will create a new file if the file doesn't exist
# w -> overwrite
# a -> will not overwrite

# 1

'''
f = open("source.txt","w")
f.write("hello how are you?")
f.close()
'''

# 2

'''
f = open("source.txt","a")
f.write("\nthis is python training")
f.close()
'''

# 3

'''
f = open("new_file.txt","w") # file doesnt exist, so create new one
f.write("this is new file!!")
f.close()
'''

# 4
'''
f = open("india.txt")
lines = f.readlines()
vowels = []
words = []

for i in lines:
    for j in i:
        if j in "aeiouAEIOU":
            vowels.append(j)
        elif j == " ":
            words.append(i)
        else:
            pass

print(len(vowels))
print(len(words))
print(len(lines))
f.close()
'''

# 5

'''
f = open("india.txt")
lines = f.readlines()
f1 = open("abc.txt","w")
for i in lines:
    f1.write(i.capitalize())
f.close()
f1.close()
'''


# 1 -> what is r+, w+ and a+ mode in txt file handling python
### r+ -> write + 0th pos + not overwrite the file
### w+ -> read  + 0th pos + overwrite
### a+ -> read  + nth pos + append at end

# 2 -> what is seek and tell() in txt file handling python
### tell() -> return the cursor pos while read/write
### seek(offset,whence) -> to move the cursor to another pos
#### offset -> how many pos to move(+ -> right,- -> left)
#### whence -> 0,1,2 (0-> begin, 1-> current pos, 2 -> end )

# 3 -> what is with keyword in txt file handling python
# with open() as file
# exception handling, file termination

# 4 -> what is the default syntax of pritn() in python
### print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# ex
'''
f1 = open("abc.txt","r+")
print(f1.readline())
f1.write("hello nandha")
print(f1.tell())
f1.close()
'''

# ex
'''
file = open('def.txt', 'a') 
try: 
    file.write('Lorem ipsum') 
finally: 
    file.close()
'''

# ex

with open("abc.txt","a") as file:
    file.write("Lorem ipsum")

# ex
# def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
#
a = 10
b = 20
print("a =", a ,"b =", b) # 4 objects , defaut -> sep = ' ', end = '\n', file=sys.stdout, flush= false
