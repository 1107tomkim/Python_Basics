# Creating a simple list
from hashlib import new
from pickletools import stringnl_noescape_pair


my_friends = ["Mike", "Sam", "John", "Timmy", "James"] # This is the list that we created
print(my_friends) # This will print out the whole list as an entirety


# More Strings
my_string = ["Tommy", 3, False]
print(my_string) # List can have multiple elements such as Strings, Integer, or a Boolean 

# Index of lists
string_index = ["0", "1", "2", "3"] # The number inside the list represents the index of the items inside the list
print(string_index[0]) # This print statement with the list[index number] will fetch only that specific element inside the list
print(string_index[1])
print(string_index[2])
print(string_index[3])

# Index of list with string
new_string_index = ["Hello", "World", 153, False, True] 
# Printing the string element "World" would be in index 1
print(new_string_index[1])
# Printing the integer element 153 would be in index 2
print(new_string_index[2])
# Printing the boolean element True would be in index 4
print(new_string_index[4])

# You can go through the list from the back by using the " - int value "
traverse_list = ["My", "Name", "is", "Tommy"]
print(traverse_list[-1]) # This will print the first element at the end of the list

# You can grab multiple element from a list by using the list[ start : end ]
traverse_list = ["My", "Name", "is", "Tommy"]
print(traverse_list[0:1])
print(traverse_list[0:2])   # It is important to keep in mind that the start index will be where
print(traverse_list[0:3])   # it starts, and is included, whereas the end index is where it ends
print(traverse_list[0:4])   # but excludes that index element.

# You can also leave the ending index a blank stating that you want to simply grab everything til the end
traverse_list = ["My", "Name", "is", "Tommy"]
print(traverse_list[0:])
print(traverse_list[1:])
print(traverse_list[2:])
print(traverse_list[3:])

# Lists can also be updated by accessing that certain index
traverse_list = ["My", "Name", "is", "Tommy"]
#           index 0      1       2       3
traverse_list[3] = "John"
print(traverse_list[0: ])     
