# CSV file handling
# Comma separated values

import csv

# Read data from the csv file
'''
f = open("source.csv","r")
data = list(csv.reader(f))
f.close()

# column
for i in data:
    print(i[0])
'''

# write data into csv file
'''
f = open("source.csv","w",newline="") # newline to ignore newline for each writerow func call

obj = csv.writer(f)
obj.writerow(["sam","sam@email.com"])
obj.writerow(["john","john@email.com"])

f.close()
'''
