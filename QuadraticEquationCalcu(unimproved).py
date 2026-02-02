#MARC RODEN D. FAMERO (BSIT 1-3)
#Problem I: Quadratic Equation Calculator
import math

a = float(input("ENTER VALUE FOR A = "))
b = float(input("ENTER VALUE FOR B = "))
c = float(input("ENTER VALUE FOR C = "))

d = math.sqrt(b*b-4*a*c)
x1 = (-b+d) / (2*a)
x2 = (-b-d) / (2*a)

print (d)
print (x1, x2)

#======END OF PROGRAM======
