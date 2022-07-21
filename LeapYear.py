
x = int(input("Year \n"))

if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("Is a leap year")
        else:
            print("Isn't a leap year")
    else:
        print("Isn't a leap year")

