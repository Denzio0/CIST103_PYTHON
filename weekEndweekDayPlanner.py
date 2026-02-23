#PYTHON PRACTICE
#WEEKEND/WEEKDAY ACTIVITY PLANNER

while True:
    try:
        dayInt = str(input("ENTER DAY OF THE WEEK: "))
        dayPerm = dayInt.lower()

        match (dayPerm):
            case "monday":
                print ("Suggested Activity: Study Programming")
            case "tuesday":
                print ("Suggested Activity: Attend Online Lecture")
            case "wednesday":
                print ("Suggested Activity: Group Project Work")
            case "thursday":
                print ("Suggested Activity: Gym / Exercise")
            case "friday":
                print ("Suggested Activity: Movie Night")
            case "saturday":
                print ("Suggested Activity: Outdoor Adventure")
            case "sunday":
                print ("Suggested Activity: Rest and Relax")
            case _:
                       print ("Invalid day entered")

    except (ValueError):
        print ("Invalid String Input")
    
