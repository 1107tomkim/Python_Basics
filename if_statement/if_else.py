# else statement is used after an if statement to operate if the "if" statement was not true.


is_female = False
if is_female: # <-  the function will first check to see if this statement is true
    print("I am a female") # <- if the "if" statement was true, then it will print this and ignore the rest of the code
else: # <- if the "if" condition was not true, then it will come to the "else" statement
    print("I am a male!") # <- and automatically print the string attached with the "else" statement