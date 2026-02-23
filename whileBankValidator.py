#PYTHON PRACTICE
#WHILE LOOP - BANK WITHDRAWAL MONITOR

balance = 100
i = 1

while i <= 10:
    balance -= 15

    if  balance <= 0:
        print ("Account Empty")
        balance = 0
        print (f"transaction {i} | Remaining Balance {balance}")
        break

    elif balance <= 40:
        print ("Low Balance Warning")
        print (f"transaction {i} | Remaining Balance {balance}")

    else:
        print (f"transaction {i} | Remaining Balance {balance}")

    i +=1

print ("=======SYSTEM TERMINATED========")

    
