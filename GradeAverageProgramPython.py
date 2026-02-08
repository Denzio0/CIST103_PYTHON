#GRADE AVERAGE PROGRAM USING CONDITIONALS IN PYTHON
#MARC RODEN FAMERO BSIT 1-3

stuGrades1 = float(input("ENTER GRADE FOR 1: "))
stuGrades2 = float(input("ENTER GRADE FOR 2: "))
stuGrades3 = float(input("ENTER GRADE FOR 3: "))

sumGrades =  stuGrades1 + stuGrades2 + stuGrades3
aveGrades = float(sumGrades / 3)

print ("YOUR AVERAGE IS: ", aveGrades)

if  aveGrades >= 98 and aveGrades <= 100:
    print ("WITH HIGHEST HONORS")

elif  aveGrades >=95:
    print ("WITH HIGH HONORS")

elif aveGrades >=90:
    print ("WITH HONORS")

elif aveGrades >=75:
    print ("PASSED")

elif  aveGrades >=51:
    print ("FAILED")

else:
    print ("invalid Grades. Try Again!")

print ("======END OF GRADING PROGRAM=======")
