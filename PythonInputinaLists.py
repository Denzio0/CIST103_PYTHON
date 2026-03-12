#PYTHON PRACTICE INPUT IN A LIST
cocTroop = []
numTroop = int(input("HOW MANY TROOP TYPES: "))

for x in range (numTroop):
    nameTroop = input(f"NAME OF THE TROOP {x + 1} : ")
    cocTroop.append(nameTroop)

print ("THE TROOPS YOU ENTERED ARE ", str(cocTroop))
