#PYTHON PRACTICE
#INCREMENT AND DECREMENT

while True:
    try:
        curTemp = int(input("ENTER CURRENT TEMPERATURE: "))
        incTemp = int(input("Increase by: "))
        decTemp = int(input("Decrease by:"))

        if incTemp < 0 or decTemp <0:
            print ("Temperature adjustments can be positive or zero only.")
            break

        curTemp -= decTemp
        curTemp += incTemp

        if curTemp < -273:
            print ("Error: Temperature too low")
        else:
            print ("Final Temperature: ", curTemp, "°C")

    except (ValueError):
        print("INVALID INTEGER INPUT")
