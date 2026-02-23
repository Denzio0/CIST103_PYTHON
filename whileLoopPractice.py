#PYTHON PRACTICING
#WHILE LOOP

#indentation = important as it tells what is included in the loop
#while loop - iterate as long as the value is "TRUE"

mmrHero = int(input("ENTER HERO MMR FOR VERIFICATION: "))

while mmrHero < 20: #20 is excluded (endpoints are excluded)
    print ("STILL NOT ENOUGH: ", str(mmrHero))
    mmrHero +=1

else: #done when the loop ends
    print("THE MMR HERO IS NOW ENOUGH: ", mmrHero)
