from math import * # This is a module, which allows us to do a lot more things within our program that is imported from pre-created functions

# Python function abs() -> Absolute value
my_number = -20
print(my_number) # This will give you the proper output of the negative integer
print(abs(my_number)) # This will return the value 20 because absolute value makes all integer positive / real number
print()
print("____________________________________________________") 

# Python function pow() -> Power
my_number = 5
print(pow(5,2)) # The first value taken in "5" is the number youre wanting to use, second value "2" declares the power value -> 5^2
print(pow(my_number,2)) # Using pre-declared int val to put into pow function
print("____________________________________________________") 

# Python function max() -> Find the largest number through the numbers that are passed
print(max(5, 3, 2, 7, -1, 13, 8, -4, 123))

# Python function min() -> Find the smallest number through the number that are passed
print(min(5, 3, 2, 7, -1, 13, 8, -4, 123))

# Python function round() -> Rounds up or down the number depending on the decimal value
print(round(3.2)) # Will round down since it is below .5
print(round(3.5)) # Will round up since it is equal to or above .5

# Python function floor() -> Rounds down the number regardless of the decimal value
print(floor(3.6))

# Python function ceil() -> Rounds up the number regardless of the decimal value
print(ceil(3.1))

# Python function sqrt() => Finds the square root value of the number passed through
print(sqrt(4))
print(sqrt(9))
print(sqrt(25))