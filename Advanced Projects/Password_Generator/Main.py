#/usr/bin/python3

from Database import sqldb
from PasswordGenerator import PasswordGenerator

import os

print("Welcome to PassGru\n".center(os.get_terminal_size().columns))
User_Input = int(input("[1] Save a new password\n[2] Retrive Password\n[3] Generate a new password\nInput: "))


if User_Input == 1:

	website = input("Website URL: ").lower()
	Username = input("Username: ").lower()
	Password = input("Password: ").lower()

	# Logic for inputing  the data into the database
	sqldb = sqldb(website, Username, Password)
	sqldb.__addData__()


elif User_In == 2:

	website = input("[+] Please Enter your Website name: ")
	UserName = "None"
	Password = "None"

	# Logic for getting the username and password from the database
	sqldb = sqldb(website, Username, Password)
	sqldb.__FetchData__()


elif User_In == 3:
	char = int(input("How many letter do you want in you password(Ex. 15): "))

	# Logic to generate the password
	PasswordGenerator.__PasswordGenerate__(Char)

else:
	print("Retry again...Invalid Input")


