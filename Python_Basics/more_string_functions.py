# len(string) -> will grab the length of the string 
my_phrase = "This is my own phrase!"
print(len(my_phrase))

# You can grab a certain index of a string by accessing it via string[index]
# Keep in mind, index starts from 0
print(my_phrase[3])

# string.index("Character you're searching for")
# This function .index will give you the index of the character or string you are wanting to search for
# Keep noted, that the index will be the first match that the code finds while iterating through the string.
print(my_phrase.index("This"))
print(my_phrase.index("is"))
print(my_phrase.index("m"))

# string.replace("What you want to replace", "What you want to put instead")
# .replace function takes in 2 parameters, and allows you to change something in a string to something else
switch_phrase = "I love apples, they are delicious!"
print(switch_phrase)
print(switch_phrase.replace("apple", "banana"))
