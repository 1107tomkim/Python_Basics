# Creating a more complex calculator

num1 = float(input("Enter first number: "))
op = input("Enter the operator you want to use: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Operator not found")
    