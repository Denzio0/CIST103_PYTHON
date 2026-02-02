#MARC RODEN D. FAMERO (BSIT 1-3)
#Problem I: Quadratic Equation Calculator
import cmath

a = float(input("ENTER VALUE FOR A = "))
b = float(input("ENTER VALUE FOR B = "))
c = float(input("ENTER VALUE FOR C = "))

d = cmath.sqrt (b**2-4*a*c)
x1 = (-b+d) / (2*a)
x2 = (-b-d) / (2*a)

print (d)
print (x1, x2)

#======END OF PROGRAM======
