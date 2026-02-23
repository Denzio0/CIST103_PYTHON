#PYTHON PRACTICE
#FOR LOOP PRACTICE

numOrd = int(input("ENTER NUMBER OF ORDERS: "))
i = 1
finalSum = 0

for i in range (numOrd):
    ordQ = int(input(f"ENTER ORDER {i +1} QUANTITY: "))
    
    if ordQ < 0:
        print ("Invalid Quantity")
        continue

    elif ordQ == 0:
        print ("Order Cancelled")
        continue

    elif ordQ > 500:
        print ("Fraudulent Order Detected")
        break

    elif ordQ < 50:
         print ("Small Order")

    elif ordQ < 200:
        print ("Medium Order")

    elif ordQ < 501:
        print ("Large Order")

    finalSum += ordQ 

print ("System Stopped")
print (f"Total Valid Orders: {numOrd}")
print ("Total Quantity Processed:" , finalSum)


            

        
    
    
