#PYTHON PRACTICE TIMER WITH FORMAT
import time

while True:
    try:
        myTime = int(input("ENTER TIME IN SECONDS: "))

        for x in range (myTime, 0, -1):
            seconds = x % 60
            minutes = int((x / 60) % 60)
            hours = int(x / 3600)
            print (f" {hours:02}: {minutes:02}: {seconds:02}")
            time.sleep(1)

        print ("TIMES UP!")
        break
    except (ValueError, TypeError):
        print ("INVALID TIMER INPUT! TRY AGAIN!")
    
