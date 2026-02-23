# MARC RODEN D. FAMERO  BSIT1-3
# DATA STRUCTURES AND ALGORITHM

while True:
    print("\nPreview of Patterns:\n")

    print("1.)")
    for i in range(5):
        for y in range(5):
            print(" * ", end="")
        print()
    print()

    print("2.)")
    for i in range(1, 7):
        print(" " * ((7 - i) + 1) + "* " * i)
    print()

    print("3.)")
    for i in range(1, 7):
        for y in range(1, i):
            print(y, end=" ")
        print()
    print()

    print("4.)")
    for i in range(5, 0, -1):
        print("  " * (i - 1), end="")
        for j in range(i, 6):
            print(j, end="")
        print()
    print()

    # Pattern selection with error handling
    while True:
        try:
            choice = int(input("Select pattern (1-4) to display: "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid choice. Enter a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Enter an integer from 1 to 4.")

    if choice == 1:
        print("\nYou selected Pattern 1:")
        for i in range(5):
            for y in range(5):
                print(" * ", end="")
            print()

    elif choice == 2:
        print("\nYou selected Pattern 2:")
        for i in range(1, 7):
            print(" " * ((7 - i) + 1) + "* " * i)

    elif choice == 3:
        print("\nYou selected Pattern 3:")
        for i in range(1, 7):
            for y in range(1, i):
                print(y, end=" ")
            print()

    elif choice == 4:
        print("\nYou selected Pattern 4:")
        for i in range(5, 0, -1):
            print("  " * (i - 1), end="")
            for j in range(i, 6):
                print(j, end="")
            print()

    #Yes/No validation
    while True:
        cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if cont == "yes":
            break
        elif cont == "no":
            print("PROGRAM END")
            exit()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
