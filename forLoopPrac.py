#PYTHON PRATICE
#PYTHON FOR LOOP
#indentation - used to determine what is included in the loop
#for loop - iterate the block, for a certain amount of times, as long as the conditions  are FALSE

pcComp = ["Mouse", "Keyboard", "CPU", "Motherboard", "Monitor", "Drives", "Fans"]
#for every x in ___________
for x in pcComp:
    print (x)
    if x == "Mouse":
        print ("AN OPTICAL MOUSE")
    elif x == "Keyboard":
        print ("IT MUST BE A MECHANICAL ONE")
    else:
        break

else:
    print ("NO MORE COMPONENTS") #prints once when the loop ends
