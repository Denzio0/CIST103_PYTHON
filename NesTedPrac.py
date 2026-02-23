#PYTHON PRACTICE
#NESTED LOOP PRACTICE
row = int(input("ENTER NUMBER OF ROWS: "))

for i in range (1,row + 1, 1):
    print('*'*i)

for i in range (row, 0 , -1):
    print('*'*i)

for i in range (1,row + 1, 1):
    print(" " *((row - i)+1) + '*'*i)

j = 1
for i in range (row, 0, -1):
    print(" "*j  + '*'*i)
    j += 1


