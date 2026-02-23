#PYTHON PRACTICE
#FOR LOOP CHALLENGE - ACCOUNT AUTHENTICATION

userName = ["Denz", "Shikii", "Ruperts", "Blue"]
passWord = ["abc123", "xyzvgh", "0123", "0987"]

inUser = input("ENTER USERNAME: ")
inPass = input("ENTER PASSWORD: ")

for z in userName and passWord:
    if inUser == userName [0] and inPass == passWord[0]:
        print (f"Welcome! {inUser}")
        break

    elif inUser == userName [1] and inPass == passWord[1]:
        print (f"Welcome! {inUser}")
        break

    elif inUser == userName [2] and inPass == passWord[2]:
        print (f"Welcome! {inUser}")
        break

    elif inUser == userName [3] and inPass == passWord[3]:
        print (f"Welcome! {inUser}")
        break
   
    else:
        print (f"Account {inUser} is not Found!")
        break
