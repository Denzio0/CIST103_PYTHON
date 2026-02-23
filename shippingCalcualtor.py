#PYTHON PRACTICE
#SHIPPING FEE CALCULATOR

while True:
    try:
        codeLoc = int(input("INPUT DELIVERY LOCATION CODE: "))
        totalPur = int(input("AMOUNT OF PURCHASE: "))
        shipFee = 0
        locPerm = ""

        match (codeLoc):
            case 1:
                shipFee = 50
                if totalPur >= 3000:
                    shipFee = 0
                elif totalPur >= 0:
                    print ("INVALID PURCHASE AMOUNT")
                locPerm = "METRO MANILA"

                print (locPerm)
                print ("Shipping Fee: ₱", shipFee)
                print ("Total Payment: ₱", (shipFee + totalPur))
                
            case 2:
                shipFee = 100
                if totalPur >= 3000:
                    shipFee = 0
                elif totalPur >= 0:
                    print ("INVALID PURCHASE AMOUNT")
                locPerm = "LUZON PROVINCE"

                print (locPerm)
                print ("Shipping Fee: ₱", shipFee)
                print ("Total Payment: ₱", (shipFee + totalPur))

            case 3:
                shipFee = 150
                if totalPur >= 3000:
                    shipFee = 0
                elif totalPur >= 0:
                    print ("INVALID PURCHASE AMOUNT")
                locPerm = "VISAYAS"

                print (locPerm)
                print ("Shipping Fee: ₱", shipFee)
                print ("Total Payment: ₱", (shipFee + totalPur))

            case 4:
                shipFee = 180
                if totalPur >= 3000:
                    shipFee = 0
                elif totalPur >= 0:
                    print ("INVALID PURCHASE AMOUNT")
                locPerm = "MINDANAO"

                print (locPerm)
                print ("Shipping Fee: ₱", shipFee)
                print ("Total Payment: ₱", (shipFee + totalPur))

            case _:
                print ("INVALID LOCATION CODE")

    except (ValueError):
        print ("INVALID INPUT")

        
