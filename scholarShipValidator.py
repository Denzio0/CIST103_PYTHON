#PYTHON PRACTICE
#UNIVERSITY SCHOLARSHIP VALIDATOR

while True:
    try:
        aveGrades = int(input("ENTER YOUR STUDENT AVERAGE: "))
        extraCur = int(input("ENTER NUMBER OF EXTRA CURRICULAR ACTIVITIES: "))

        if aveGrades >= 90:
            if extraCur >=2:
                print ("Full Scholarship")
                print ("")

        elif aveGrades >= 85:
            if extraCur == 1:
                print ("Partial Scholarship")
                print ("")

        elif aveGrades >= 80:
            print ("Book Allowance Grant")
            print ("")

        elif aveGrades < 80:
            print ("No Scholarship Awarded. Try Again Next Time!")
            print ("")

        else:
            print ("INVALID INPUT OF AVERAGE AND/OR NUMBER OF ACTIVITIES ATTENDED")
            print ("")

    except (ValueError):
        print ("IVALID! INPUT ONLY INTEGER")
        print ("")
