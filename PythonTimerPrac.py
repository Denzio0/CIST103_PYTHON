#PYTHON PRACTICE TIME
import time

while True:
    try:
        runTime = True
        seconds = 1
        end = int(input("ENTER TIMER IN SECONDS: "))

        while runTime:
            print (seconds, end=" ")
            time.sleep(1) #DELAYS THE COUNETR BY 1 SECOND
            seconds +=1
            if seconds > end:
                print ("TIME'S UP!")
                break

        print ("GOOD WORK!")
        break
    except (ValueError, TypeError):
        print ("INVALID TIMER INPUT")
    
while True:
    try:
        runTime = True
        seconds = int(input("ENTER TIMER IN SECONDS: "))
        end = 0

        while runTime:
            print (seconds, end=" ")
            time.sleep(1) #DELAYS THE COUNETR BY 1 SECOND
            seconds -=1
            if seconds <= end:
                print ("TIME'S UP!")
                break

        print ("GOOD WORK!")
        break
    except (ValueError, TypeError):
        print ("INVALID TIMER INPUT")
    
