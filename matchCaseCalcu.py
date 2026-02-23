#PYTHON PRACTICE
#SIMPLE MATCH CASE CALCULATOR
while True:
    try:
        num1 = int(input("ENTER FIRST NUMBER: "))
        num2 = int(input("ENTER SECOND NUMBER: "))
        oP = str(input("ENTER OPERATION TO USE (+, -, *, /): "))
        finalAns = 0

        match oP:
            case "+":
                 finalAns = num1 + num2
                 print (finalAns)

            case "-":
                 finalAns = num1 - num2
                 print (finalAns)

            case "*":
                 finalAns = num1 * num2
                 print (finalAns)

            case "/":
                 if num2 == 0:
                     print("CANNOT BE DIVIDED BY ZERO")
                 else:
                     finalAns = num1 / num2
                     print (finalAns)

            case _:
                 print("INVALID INPUT")
         
    except (ValueError):
        print("INVALID INPUT")
         
         
