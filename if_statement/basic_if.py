# If statement are used to execute function when certain statement is either true or false.

# Creating a boolean variable to test if statements condition
from operator import truediv


is_male = True
is_female = False

if is_male:
    print("You are a male")

# In this statment, because the condition is false, it will not do the print statement.
if is_female: # <- checks to see if the condition is true
    print("You are not a female") # <- if it passed the previous condition check, it will run this function
