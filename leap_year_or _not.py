while True:
    year=int(input("Enter the year you want to check:"))
    if year%4==0 :
        print(year,"is a leap year")
    elif  year%100==0:
        print(year,"It is not a leap year")
    elif year%400==0:
        print(year,"It is a leap year")
    else:
        print(year,"It is not a leap year")
    choice = input("Do you want to check another year? (yes/no): ").lower()

    if choice == "no":
        print("Program exited.")
        break