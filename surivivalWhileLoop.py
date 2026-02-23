#PYTHON PRACTICE
#WHILE LOOP CHALLENGE - DUAL RESOURCE SURVIVAL SYSTEM

oxygen = 100
energy = 60
i = 1

while i < 20:
    oxygen -= 7
    energy -=5

    if oxygen < 0 or energy < 0:
        oxygen == 0 and energy == 0

    elif oxygen <= 15 and energy <= 15:
        print ("System Failure")
        break

    elif energy <= 20:
        print ("Critical Energy Level")
        print (f"Cycle {i} | Oxygen: {oxygen} | Energy: {energy}")

    elif oxygen <= 30:
        print ("Critical Oxygen Level")
        print (f"Cycle {i} | Oxygen: {oxygen} | Energy: {energy}")

    else:
        print (f"Cycle {i} | Oxygen: {oxygen} | Energy: {energy}")

    i +=1

else:
    print ("Mission Time Limit Reached")
