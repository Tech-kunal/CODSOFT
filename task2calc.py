def SimpleCalculator():
    print("Simple Calculator : ")
    print()
    print()
    print("Press 1 For Addition")
    print("Enter 2 For Subtract")
    print("3)Multiplication")
    print("Press 4 For Division")
    choice = input(" Enter choice : ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The Result of Addition: {num1 + num2}")

        elif choice == '2':
            print(f"Subtraction: {num1 - num2}")

        elif choice == '3':
            print(f"Multiplication of two no: {num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2!= 0:
                print(f"The Division Result is: {num1 / num2}")
            else:
                print("Error! Division by zero.")

    else:
        print("Invalid input")

SimpleCalculator()