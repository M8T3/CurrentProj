num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))
if num % check == 0:
    if num % 4 == 0:
        print(str(num) + " is a multiple of " + str(check))
        print(str(num) + " is a multiple of 4.")
    elif num % 2 == 0:
        print(str(num) + " is a multiple of " + str(check))
        print(str(num) + " is even.")
    else:
        print(str(num) + " is a multiple of " + str(check))
        print(str(num) + " is odd.")
elif num % check != 0:
    if num % 4 == 0:
        print(str(num) + " is not a multiple of " + str(check))
        print(str(num) + " is a multiple of 4.")
    elif num % 2 == 0:
        print(str(num) + " is not a multiple of " + str(check))
        print(str(num) + " is even.")
    else:
        print(str(num) + " is a not multiple of " + str(check))
        print(str(num) + " is odd.")

