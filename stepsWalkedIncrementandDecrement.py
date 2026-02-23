#PYTHON PRACTICE
#INCREMENT AND DECREMENT STEPS WALED

while True:
    try:
        curSteps= int(input("ENTER STARTING STEPS: "))
        incSteps= int(input("STEPS WALKED: "))
        decSteps = int(input("STEPS LOST:"))

        if incSteps< 0 or decSteps<0:
            print ("Steps can only be positive or zero only.")
            break

        curSteps-= decSteps
        curSteps+= incSteps

        if curSteps < 0:
            print ("Error: Step count cannot be negative")
        else:
            print ("Final Steps: ", curSteps, "Steps")

    except (ValueError):
        print("INVALID INTEGER INPUT")
