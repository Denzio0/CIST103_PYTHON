#ADMIN AND PASSWORD CONDITIONALS ACTIVITY

userName = input("ENTER THE ADMIN USERNAME: ")
passWord = input("ENTER ADMIN PASSWORD: ")

userLow = userName.casefold() #CONVERTS CASES FOR FUNCTIONALITY

if userLow== "admin" and passWord == "1234":
    print ("ACCESS GRANTED")
elif userLow == "guest" and passWord == "abcd":
     print ("VIEWING MODE GRANTED")
else:
    print ("ACCESS DENIED")

print ("======END OF PROGRAM=====")
