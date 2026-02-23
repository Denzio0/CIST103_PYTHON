#PYTHON PRACTICE
#FOR LOOP CHALLENGE - SECURITY CODE SCANNER

for i in range (1, 51):
    if (i % 4) == 0:
        continue

    elif(i % 9) == 0:
        print ("Suspicious Code Detected")
        break

    elif(i%2) == 0:
        print (f"Valid Even Code: {i}")

    elif(i%2) != 0:
        print (f"Valid Odd Code: {i}")

    else:
        print ("INVALID NUMBER")

    
        
