def operation():
    choice = input("Enter your choice: ")
    
    if choice == "1" :
        #Addition
        print("\nAddition")
        while True:
            num1 = float(input("Enter a value 1 : "))
            num2= float(input("Enter a value 2 : "))
            print("Result: ", num1 + num2)
            if input("Do you want to continue adding?(y/n) ").lower() == "n":
                break
            else:
                continue
        return 1
    elif choice == "2" :
        #Substraction
        print("\nSubstraction")
        while True:
            num1 = float(input("Enter a value 1 : "))
            num2= float(input("Enter a value 2 : "))
            print("Result: ", num1 - num2)
            if input("Do you want to continue subtracting?(y/n) ").lower() == "n":
                break
            else:
                continue
        return 1
    elif choice == "3" :
        #Multiplication
        print("\nMultiplication")
        while True:
            num1 = float(input("Enter a value 1 : "))
            num2= float(input("Enter a value 2 : "))
            print("Result: ", num1 * num2)
            if input("Do you want to continue multiplying?(y/n) ").lower() == "n":
                break
            else:
                continue
        return 1
    elif choice == "4" :
        #Division(accurate)
        print("\nDivision(accurate)")
        while True:
            num1 = float(input("Enter a value 1 : "))
            num2= float(input("Enter a value 2 : "))
            print("Result: ", num1 / num2)
            if input("Do you want to continue dividing?(y/n) ").lower() == "n":
                break
            else:
                continue
        return 1
    elif choice == "5":
        #Division with Remainder
        print("\nDivision with Remainder")
        while True:
            num1 = float(input("Enter a value 1 : "))
            num2= float(input("Enter a value 2 : "))
            print("Quotient: ", num1 // num2)
            print("Remainder: ", num1 % num2)
            if input("Do you want to continue dividing with remainder?(y/n) ").lower() == "n":
                break
            else:
                continue
        return 1
    elif choice == "6":
        #Exponential multiplication
        print("\nExponential multiplication")
        while True:
            num = float(input("Enter a value : "))
            exponent = float(input("Enter a value to add as exponent : "))
            print("Result: ", num ** exponent)
            if input("Do you want to continue exponential multiplication?(y/n) ").lower() == "n":
                break
            else:
                continue
        return 1
    elif choice == "7":
        return 0
    else:
        print("Invalid Input.")
        return 1

def calculator():
    print("For Addition enter:                   1")
    print("For Subtraction enter:                2")
    print("For Multiplication enter:             3")
    print("For Division enter:                   4")
    print("For Division with Remainder enter:    5")
    print("For Exponential Multiplication enter: 6")
    print("To Exit enter:                        7")
    
    while True:
        user = operation()
        if user == 0:
            break
        else:
            continue


calculator()
