# Print the menu
print("=== CALCULATOR ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("0. Exit")
choice = input("Choose an option: ")
print("You chose:", choice)
# Read the choice and print it
if choice == '1'or choice == '2' or choice == '3' or choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        result = num1 + num2
        print("Result:", result)
    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero") 
