# JSON Files

# dump() and load()

'''
import json

dict1 = {101:{"Name":"sam","Amount":10000},102:{"Name":"john","Amount":20000}}

# Write data into json file

f = open("file.txt","w")
json.dump(dict1,f,indent=4)
f.close()

# Read data from the json file

f = open("file.txt", "r")
data = json.load(f)
f.close()
print(data)

'''
