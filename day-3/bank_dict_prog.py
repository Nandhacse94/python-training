# Bank dict project
# sample op

# 1. new customer 2. ex 3. exit
# name , address, age, account (savings,credit), amount , account num (check exists)

# ex
# 1. check bal 2. withdraw(subtract and update) 3. deposit (add and update)


# acc_num is key: {name:,addr,age,acc,balance,acc_num}

data = {}

import json

def load_json():
    f = open("bank_file.txt","r")
    data = json.load(f)
    f.close()
    return data

def dump_json(data):
    f = open("bank_file.txt","w")
    json.dump(data,f,indent=4)
    f.close()
    
def newAccount(data):
    acc_num = int(input("Enter your account number:")) # key
    
    while data.get(acc_num):
        print("Account Number Exists! Enter different account number:")
        acc_num = int(input("Enter your account number:")) # key

    # value
    list1 = ["Name","Address","Age","Amount"]

    name = input("Enter your name:")
    while name.isalpha() == False:
        print("Invalid Name! Enter right one please")
        name = input("Enter your name:")
        
    addr = input("Enter your Address:")
    
    age = input("Enter your age:")
    while age.isnumeric() == False or int(age) < 18 or int(age) > 120 :
        print("Invalid age! please enter right one!")
        age = input("Enter your age:")
        
    amt = input("Enter  Amount:")
    while amt.isnumeric() == False or int(amt) < 100:
        print("Invalid amount! Our Bank minimum balance is 100.")
        amt = input("Enter  Amount:")

    # storing data into dictionary
    list2 = [name,addr,int(age),int(amt)]

    data[acc_num] = dict(zip(list1,list2))

    print(data)

def amountWithdraw(acc_num,data):
    print("---- Withdraw process ----")
    amt = float(input("Enter the amount to withdraw:"))
    if amt > data[acc_num]["Amount"]:
        print("Not enough balance! please enter right amount again")
        amt = int(input("Enter the amount to withdraw:"))
    else:
        bal = data[acc_num]["Amount"]
        data[acc_num]["Amount"] = bal - amt
        print("Balance Amount in your account is:",data[acc_num]["Amount"])
    return data

def amountDeposit(acc_num,data):
    print("---- Deposit ----")
    amt = float(input("Enter the amount to Deposit:"))
    data[acc_num]["Amount"] += amt
    print("Balance Amount in your account is:",data[acc_num]["Amount"])
    return data

    
def existingCust(data):
    acc_num = (input("Enter your account number to fetch your details:"))
    
    if acc_num in data:
        print("---- Record Found ----")
        while True:
            print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
            ch = int(input("Enter your choice:"))

            if ch == 1:
                print("Your Account Balance is ",data[acc_num]["Amount"])
            elif ch ==2:
                if data[acc_num]["Amount"] <= 0:
                    print("There is no amount to withdraw from your account!")
                    pass
                data = amountWithdraw(acc_num,data)
                
            elif ch == 3:
                data = amountDeposit(acc_num,data)
                
            elif ch == 4:
                break
            else:
                print("Invalid choice:")
    else:
        print("---- Record Not Found ----")
            
while True:
    print("1. New Customer:")
    print("2. Existing Customer:")
    print("3. Exit:")
    ch = int(input("Enter your choice:"))
    

    if ch == 1:
        data = load_json()
        newAccount(data)
        dump_json(data)
        data.clear()

    elif ch == 2:
        data = load_json()
        existingCust(data)
        dump_json(data)
        data.clear()

    elif ch == 3:
        print("Thanks for contacting Bank!")
        break
    else:
        print("Invalid Choice")
        
