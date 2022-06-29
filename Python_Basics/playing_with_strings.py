# \n -> is a newline, meaning that usage of \n will create a new line and post everything after in a new line.
# The following will output Python in one line and Academy in another line.
print("Python \nAcademy")

# printing a preset value of a phrase by storing in a variable as a string
phrase = "Python Academy"
print(phrase)

# Using concatenation to create a new string by adding more to the previous string
print(phrase + " is cool!")

# Prebuilt string function to play with strings!

# (string).lower() takes everything in the string and converts it to lowercase
allcap_string = "THIS IS A CAPITALIZED SENTENCE!"
print(allcap_string.lower())

# (string).upper() takes everything in the string and converts it to uppercase
lowercase_string = "this is a lowercase sentence!"
print(lowercase_string.upper())

# (string).isupper() takes the string and checks if everything is uppercase
# The function is a booleon function returning only true or false depending on the case
print(allcap_string.isupper())

# (string).islower() takes the string and checks if everything is lowercase
# The function is a booleon function returning only true or false depending on the case
print(lowercase_string.islower())

# You can use multiple functions together
# I.E -> Using (string).upper function to turn a string uppercase and checking to see if its all uppercase
print(lowercase_string.upper().isupper())
# Checking to see if the sentence is all lowercase
print(lowercase_string.upper().islower())