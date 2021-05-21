# 1. signup 2. login
# name pass

# name pass

data = {}
while True:
    print("1. Sign Up\n2. Login")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        name = input("Enter your name:")
        passwd = input("Enter your password:")
        data[name] = passwd
        
    elif ch == 2:
        name = input("Enter your name:")
        if data.get(name):
            print("name is available in the records")
            passwd = input("Enter your password:")
            if passwd == data[name]:
                print("Login Successfull!!")
            else:
                print("Invalid Password")
        else:
            print("Invalid Name! name is not available in the records")
            pass
        
    else:
        print("Invalid choice")
