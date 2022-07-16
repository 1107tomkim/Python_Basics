# when using the "and" operator inside the "if" statement, both condition has to be true in order
# for the function to pass the if statement, else it will do what the "else" statement has.


# Stating two boolean statement to test with one being true and one being false
am_female = False
am_male = True

if am_female and am_male: # This "if" statement test for two things, 1 -> if I am a female, and 2 -> if I am a male
    print("I am both female and a male!") # If both conditions are true then it will print this statement
else:
    print("I am not both male and female") # It will print this statement if the previous conditions are not true.
# This function will print the statement "I am not both male and female" because one or more of the statement in the if statement is false



# Stating two boolean statement to test with both being true
am_male = True
am_tall = True


if am_male and am_tall: # Statement to check if I am a male and I am tall
    print("I am a male and I am tall!") # If both statements are true then it will print this statement
else:
    print("I dont know what I am!") # Else it will print this statement.
# This function will print the statement "I am a male and I am tall!" because both statements are true!