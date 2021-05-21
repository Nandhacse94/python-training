# Simple List Database project

#   1) Add data -> name, phone, address
#   2) Show data -> name
#   3) Delete data


##name = []
##phone = []
##address = []

data = []

while True:
    print("1. Add data")
    print("2. Show data")
    print("3. Delete data")
    print("4. Exit")

    ch = int(input("Enter your choice:"))
    
    if ch == 1:
        n = input("Enter your name:")
        while n.isalpha() == False:
            print("Invalid name!! please try again")
            n = input("Enter your name:")
        #name.append(n)
        ph = input("Enter your phone number:")
        while ph.isdigit() != True:
            print("Invalid phone num!! please try again")
            ph = input("Enter your phone number:")
        #phone.append(ph)
        add = input("Enter your address:")
        #address.append(add)
        data.append((n,ph,add))
        print("---- DATA ADDED SUCCESSFULLY ----")

    elif ch == 2:
        n = input("Enter your name to extract your details:")
        for i in data:
            if n in i[0]:
                print("--- DATA FOUND ---")
                ind = data.index(i)
                print("Name: %s"%data[ind][0])
                print("phone: %s"%data[ind][1])
                print("Address: %s"%data[ind][2])
            else:
                print("--- DATA NOT FOUND ---")

    elif ch == 3:
        n = input("Enter your name to delete details:")
        for i in data:
            if n in i[0]:
                print("--- DATA DELETED ---")
                ind = data.index(i)
                del data[ind]
            else:
                print("--- DATA NOT FOUND ---")
    elif ch == 4:
        break
    else:
        print("Invalid Choice!!!")


        
