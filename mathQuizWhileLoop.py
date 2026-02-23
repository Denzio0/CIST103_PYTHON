#PYTHON CHALLENGE PRACTICE
#WHILE LOOP QUIZ GAME

i = 0
while i <= 9:
    sqrAns = int(input("MATH PROBLEM - WHAT IS THE SQUARE ROOT OF 121?: "))
    if sqrAns == 11:
        print ("YOU GOT THE CORRECT ANSWER!")
        break
    else:
        print ("WRONG ANSWER! YOU HAVE" , 9-i, "TRIES LEFT")
    i +=1

else:
    print ("NO MORE TRIES LEFT! GET LOST!")

print ("=======SYSTEM TERMINATED========")

