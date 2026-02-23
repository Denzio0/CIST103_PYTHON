#PYTHON PRACTICE
#ODD EVEN WHILE LOOP CHECKER

numBer = [-19, 10,11,12,13,14,15,16,17,18,19,20, 109,88,76]
i = 0 #initialize

while i < len(numBer): #used to start
    if (numBer[i] % 2 == 0):
        print ("THE EVEN NUMBERS ARE:" , numBer[i])
    else:
        print ("THE  ODD NUMBERS ARE:" , numBer[i])
    i +=1 #USED TO STOP!
