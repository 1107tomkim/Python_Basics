# This file is simply to put all the operators that are allowed in Python.
# Please feel free to add more operator as I may forget some.


# Arithmetic Operators
# +   -> Addition
def addition(num1, num2):
    return num1 + num2
print("Solution to addition function when num1 = 1 and num2 = 5 is: " + str(addition(1,5)))

# -   -> Subtraction
def subtraction(num1, num2):
    return num1 - num2
print("Solution to subtraction function when num1 = 10 and num2 = 5 is: " + str(subtraction(10, 5)))

# *   -> Multiplication
def multiplication(num1, num2):
    return num1 * num2
print("Solution to multiplication function when num1 = 2 and num2 = 2 is: " + str(multiplication(2, 2)))

# /   -> Division
def division(num1, num2):
    return num1 / num2
print("Solution to division function when num1 = 10 and num2 = 2 is: " + str(division(10, 2)))

# %   -> Modulus
def modulus(num1, num2):
    return num1 % num2
print("Solution to modulus function when num1 = 10 and num2 = 3 is: " + str(modulus(10, 3)))

# **  -> Exponentiation
def exponentiation(num1, num2):
    return num1 ** num2
print("Solution to exponentiation function when num1 = 5 and num2 = 2 is: " + str(exponentiation(5, 2)))

# //  -> Floor Division
def floor_division(num1, num2):
    return num1 // num2
print("Solution to floor division function when num1 = 5 and num2 = 2 is: " + str(floor_division(5, 2)))


#Assignment Operators
# =   -> Setting something equal to something. EX -> x = 5
my_age = 25
print(my_age)

# +=  -> Adding 
going_up = 1
print(going_up)
going_up += 1
print(going_up)

# -=  ->
going_down = 10
print(going_down)
going_down -= 1
print(going_down)

# *=  ->
multi_myself = 2
print(multi_myself)
multi_myself *= 2
print(multi_myself)

# /=  ->
divide_myself = 10
print(divide_myself)
divide_myself /= 2
print(divide_myself)
