while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("\nPress 0 for Addition")
    print("Press 1 for Subtraction")
    print("Press 2 for Multiplication")
    print("Press 3 for Division")

    choices = int(input("Enter your choice: "))

    if choices == 0:
        print("The sum of", a, "and", b, "is:", a + b)

    elif choices == 1:
        print("The difference of", a, "and", b, "is:", a - b)

    elif choices == 2:
        print("The product of", a, "and", b, "is:", a * b)

    elif choices == 3:
        if b != 0:
            print("The division of", a, "and", b, "is:", a / b)
        else:
            print("Division not allowed.")

    else:
        print("Invalid choice")

    print("\nPress 1 to Continue")
    print("Press 0 to Exit")
    option = int(input("Enter your choice: "))

    if option == 0:
        print("Thank you for using the calculator!")
        break