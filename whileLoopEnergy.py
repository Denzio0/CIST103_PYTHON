#PYTHON PRACTICE CHALLENGE
#WHILE LOOP - ENERGY DRINK TRACKER
iniEnergy = int(input("INITIAL ENERGY LEVEL: "))
actChoi = str(input("CHOOSE ACTION FOR ENERGY: 1 - Work 2 - Rest 3 - Eat 4 - Exit: "))

while  not  actChoi == "4":
    if actChoi == "1":
        iniEnergy -= 10
        print (f"YOUR FINAL ENERGY IS: {iniEnergy}")
        actChoi = (input("CHOOSE ACTION FOR ENERGY: 1 - Work 2 - Rest 3 - Eat 4 - Exit: "))
        print (f"YOUR ACTION CHOICE IS {actChoi}")

    elif actChoi == "2":
        iniEnergy += 5
        print (f"YOUR FINAL ENERGY IS: {iniEnergy}")
        actChoi = (input("CHOOSE ACTION FOR ENERGY: 1 - Work 2 - Rest 3 - Eat 4 - Exit: "))
        print (f"YOUR ACTION CHOICE IS {actChoi}")

    elif actChoi == "3":
        iniEnergy += 15
        print (f"YOUR FINAL ENERGY IS: {iniEnergy}")
        actChoi = (input("CHOOSE ACTION FOR ENERGY: 1 - Work 2 - Rest 3 - Eat 4 - Exit: "))
        print (f"YOUR ACTION CHOICE IS {actChoi}")
        
    elif iniEnergy > 100:
        print ("Energy cannot go above 100")
        actChoi = (input("CHOOSE ACTION FOR ENERGY: 1 - Work 2 - Rest 3 - Eat 4 - Exit: "))
        print (f"YOUR ACTION CHOICE IS {actChoi}")

    elif iniEnergy < 0:
        print ("Energy cannot go below 0")
        actChoi = (input("CHOOSE ACTION FOR ENERGY: 1 - Work 2 - Rest 3 - Eat 4 - Exit: "))
        print (f"YOUR ACTION CHOICE IS {actChoi}")

    else:
        print ("INVALID ACTION CHOICE")
        break

    if iniEnergy == 0:
        print ("YOU ARE TIRED!")
        break

    if iniEnergy == 100:
        print ("YOU ARE FULL TANKED!")
        break

else:
    print (f"YOUR ACTION CHOICE IS {actChoi}")
    print ("PROGRAM ENDED")
