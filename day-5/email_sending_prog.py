# Email Sending application
# Prerequiste:

# Login to gmail account -> manage your account(top right)-> security
# Less secure app access -> Turn on access

import smtplib #simple mail transfer protocol

server = smtplib.SMTP("smtp.gmail.com",587) # 1 - server address 2 - port number

# to make a secure connection
server.starttls()

print("Connected with the server!!!")

# login
username = input("Enter username:")
password = input("Enter your password:")

server.login(username, password)
print("Login Successfull")

# Send an email

receiver = input("Enter receiver's email id:")

msg = str("This is mail from nandhakumar")
server.sendmail(username,receiver,msg)
print("Mail sent successfully")
