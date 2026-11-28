# Print the menu
print("=== CALCULATOR ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("0. Exit")
choice = ""

while choice != "0":
    choice = input("Choose an option: ")

    if choice == "1":
        a = float(input())
        b = float(input())
        print(a + b)

    elif choice == "2":
        a = float(input())
        b = float(input())
        print(a - b)

    elif choice == "3":
        a = float(input())
        b = float(input())
        print(a * b)

    elif choice == "4":
        a = float(input())
        b = float(input())
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(a / b)

    elif choice == "0":
        print("End of program")

    else:
        print("Unknown option")