#LISTS AND TUPLES
specialGrades = ["Gojo Satoru", "Ryomei Sukuna", "Yuta Okkotsu", "Itadori Yuji", "Gojo Satoru", "Gojo Satoru", "Gojo Satoru"]
heavenlyRes = ["Toji Fushiguro", "Maki Zenin", "Yuki Okkotsu"]

print(specialGrades)
print ("THE STRONGEST SORCERER IS " ,specialGrades[0])
print ("THE STRONGEST OF MODULO IS " ,specialGrades[3])
print ("THE STRONGEST OF NEXT TO GOJO IS" ,specialGrades[-2]) 

print(heavenlyRes[0:3]) #endindex "3" is not counted 
print("THE SHINJUKU SHOWDOWN HAPPENS BETWEEN: " + str(specialGrades[0:2]))

#ASSIGNING ANOTHER VALUE ON LISTS
specialGrades[2] = "Geto Suguru"
print()
print(specialGrades)

print()

#LIST LENGTH
print(len(specialGrades))

print()

#LIST COUNT
print (specialGrades.count("Gojo Satoru"))
print (specialGrades.count("Choso"))

print()

#ADDING ITEMS IN A LIST (using list.append)
heavenlyRes.append("Mechamaru")
print (heavenlyRes)

print()

#ADDING ITEMS BY INSERT
heavenlyRes.insert(2, "Kokichi Muta")
print (heavenlyRes)

print()

#DELETING ITEMS IN A LIST
heavenlyRes.remove("Mechamaru")
print (heavenlyRes)

print()

#DELETING ITEMS USING POP (specific index)
heavenlyRes.pop(2)
print (heavenlyRes)

print()

#DELETING USING DEL (can delete whole list)
del heavenlyRes[2]
print (heavenlyRes)

print()

#CLEARING A LIST (can delete whoel but accessible)
heavenlyRes.clear()
print (heavenlyRes)

print()

#COPYING A LIST
jujutsu = specialGrades.copy()
print(jujutsu)

print()

#COMBINING A LIST
heavenlyRes.append("Toji Fushiguro")
kaisen = specialGrades + heavenlyRes
print (kaisen)

print()

#COMBINING LIST BY EXNTEND
jujutsu.extend(kaisen)
print (jujutsu)
print(len(jujutsu))

print()

#REVERSING LIST
kaisen.reverse()
print (kaisen)

#SORTING LISTS
plmAges = [20, 19, 23, 21, 18, 33, 88, 99]
print ("UNSORTED: " + str(plmAges))
plmAges.sort()
print ("SORTED ASCENDING: " + str(plmAges))
plmAges.sort(reverse = True)
print ("SORTED DESCENDING: " + str(plmAges))

print()

#TUPLES (A READ-ONLY LIST TYPE)
techJu = ("Red", "Blue", "Purple")
print (techJu)


#=======REVIEW 02/08/2026==========
