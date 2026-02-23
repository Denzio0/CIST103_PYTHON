#PYTHON PRACTICE
#ELECTRICITY BILL CALCULATOR

#INPUT SECTIONS
while True:
    try:
        conSump = int(input("Enter Total electricity consumption in kWh: "))
        discSenior = str(input("Senior Citizen (Yes or No): "))
        finalSump = 0

        #BILLING RULES
        if conSump > 200:
            finalSump = (conSump * 20)

        elif conSump > 100:
            finalSump = (conSump * 15)

        elif conSump >= 0:
            finalSump = (conSump * 10)
                        
        else:
            print ("Invalid electricity consumption entered.")
            print ("=======================================================")

        #SURCHARGE SECTION
        if conSump > 300:
            finalSump = finalSump + (finalSump * 0.1)
            
        #SENIOR DISCOUNT SECTION
        if  discSenior.lower() == "yes" or discSenior.upper() == "YES" or discSenior == "Yes" or discSenior == "yES" or discSenior == "YEs" or discSenior == "yeS":
            finalSump = finalSump - (finalSump * 0.05)
            print ("Total Bill: \u20B1" , float(finalSump))
            print ("=======================================================")

        else:
            print ("Total Bill: \u20B1" , float(finalSump))
            print ("=======================================================")


    except (ValueError):
        print ("INVALID INPUT, TRY AGAIN!!!")
        print ("=======================================================")
