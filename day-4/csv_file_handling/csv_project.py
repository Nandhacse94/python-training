# CSV Project
# Corona DB Management

# 1) Add data -> country, positive cases, recovered cases and deaths
# 2) Show Data
# 3) Plot data -> matplotlib # bar graph

import csv
import matplotlib.pyplot as plt


def addData():
    f = open("corona_db.csv","a",newline="")
    obj = csv.writer(f)
    country = input("Enter your country name:")
    posCase = int(input("Enter the number of positive cases:"))
    negCase = int(input("Enter the number of negative cases:"))
    recCase = int(input("Enter the number of recovered cases:"))
    deaths = int(input("Enter the number of deaths:"))
    
    curdata = [country,posCase,negCase,recCase,deaths]
    obj.writerow(curdata)
    f.close()

def showData():
    country = input("Enter your country name to fetch the details:")
    f = open("corona_db.csv","r")
    data = list(csv.reader(f))

    for i in data:
        #print(i)
        if i[0] == country:
            print("1. Country Name: %s\n2. Positive Cases: %i\n3. Negative Cases: %i\n4. Recovered cases: %i\n5. Death count: %i "%(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4])))
    f.close()

def plotData():
    f = open("corona_db.csv","r")
    data = list(csv.reader(f))

    country = []
    pos = []
    rec = []

    for i in data:
        country.append(i[0])
        pos.append(int(i[1]))
        rec.append(int(i[3]))

    print(country)
    print(pos)
    print(rec)
    
    plt.bar(country,pos)
    plt.bar(country,rec)
    plt.show()

    f.close()
    
while True:
    print("1. Add Data\n2. Show Data\n3. Plot Data\n4. Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        addData()
    elif ch == 2:
        showData()
    elif ch == 3:
        plotData()
    elif ch == 4:
        break
    else:
        print("Invalid choice!")

