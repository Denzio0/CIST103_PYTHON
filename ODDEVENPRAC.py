while True:
    try:
        x = int(input("ENTER INTEGER: "))
        y = x % 2

    
        if y == 0:
            print ("even")

        else:
            print ("odd")

    except (ValueError):
        print ("INVALID INTEGER INPUT")
