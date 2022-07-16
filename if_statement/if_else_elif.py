# if else and elif statement.
# You can add multiple elif statement to create more conditional statement

is_male = True
is_tall = True
is_funny = False

if is_male and is_tall: # Checks to see if I am a male 
    print("I am a male and I am tall!") # If ^ is true then it will print this statement.

elif is_male and not is_tall: # Else if this statement is true
    print("I am a male but I am not tall.") # ^ it will print this statement.

elif is_male and not is_funny: # Else if this statement is true
    print("I am a male but not funny") # It will print this statement

else: # If everything is not true
    print("I dont know what I am") # It will print this statement
