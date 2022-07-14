# Return keyword allows Python to return a result from a function

# Simple function that cubes an input number 
def cube_it(number): 
    return number * number * number # Using return statement to return the value of the function
print(cube_it(5)) # Calling the function and printing it.

# Setting a variable = to the function result and printing it
result = cube_it(4)
print(result)

# Keep noted, after the return statement, any code underneath within the function will not work.