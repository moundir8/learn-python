# Read two numbers

# Print the sum, difference, product and quotient
a = float(input('enter the first number:'))
b = float(input('enter the second number:'))
print(a+b)
print(a-b)
print(a*b)
if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero")