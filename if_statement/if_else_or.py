# In this file we will be using the if and else function but with the "or" condition
# The "or" condition basically states that at least one of the condition has to be true for it to pass

is_female = False
is_male = True

# This function will print out the result of the "if" statement although one of the condition is false because of the "or" statement
if is_female or is_male:
    print("I am either a male or a female!")
else:
    print("I am an alien!")