# first_list.extend(second_list), the .extend function allows you to append a list to the end of one list.

from imghdr import what

from requests import post


first_list = ["This", "is", "the", "first", "list"] # This is the list that you will extend
print(first_list)
second_list = ["This", "is", "the", "second", "list"] # This is the list that you are extending on
print(second_list)

first_list.extend(second_list) # Using the .extend() to extend the first_list to become a joint of both list
print(first_list)


# first_list.append(appending element) will essentially add the appending element to the end of the list
fruit_list = ["Apple", "Banana", "Cherry"]
print(fruit_list)
fruit_list.append("Watermelon")
print(fruit_list)

# list.insert(index position, element being added) will add the new element to a string in the given index
# pushing every other element in the list to the next index

my_list = ["1", "2", "3", "4"]
print(my_list)

# This function will essentially take the 0th index of my_list which is the element "1" and put a new element "0" in its position
# while pushing everything else to the next index
my_list.insert(0, "0")
print(my_list)

# list.remove(element you want to remove) will remove the element of the list 
what_to_remove = ["I", "Hate", "Love", "Tomato"]
what_to_remove.remove("Hate") # Removing index 1 of the list, element "Hate"
print(what_to_remove)
what_to_remove.insert(1, "Hate") # Adding back the element "Hate" To the list and pushing everything back
print(what_to_remove)

# list.clear() This function will essentially remove all the element of the list and return an empty list.
full_list = ["I", "Am", "A", "Full", "List"]
print(full_list)
full_list.clear() # Removing all the elements in the list
print(full_list)

# list.pop() This function will remove the last element on the list
popcorn = ["Pop", "The", "Popcorn", "Bag"]
print(popcorn)
popcorn.pop()
print(popcorn)

# print(list.index(element to search)) This function will allow you to search for an elements existence in the list
# as well as return the position ( index ) of the element in the list.
position_list = ["Tom", "Mike", "Shaun", "Jim"]
print(position_list.index("Tom"))
print(position_list.index("Mike"))
print(position_list.index("Shaun"))
# print(position_list.index("Jackson")) When you search for an element that does not exist in the list, it will throw you an error stating " Element is not in the list"

# print(list.count(Element)) Function will allow you to count have many of the same element is in the list
any_duplicates = ["Tom", "Mike", "Tom", "Shaun", "Jim"]
print(any_duplicates.count("Tom"))

# list.sort() Function will sort your list in alphabeticall order as well as ascending numbers
alphabet_list = ["D", "F", "C", "A", "E", "B"]
number_list = ["0", "4", "1", "3", "2"]
alphabet_list.sort()
number_list.sort()
print(alphabet_list)
print(number_list)

# list.reverse() Function will reverse the order of the list
alphabet_list = ["D", "F", "C", "A", "E", "B"]
number_list = ["0", "4", "1", "3", "2"]
alphabet_list.reverse()
number_list.reverse()
print(alphabet_list)
print(number_list)

# list.copy() Function will copy the list
original_list = ["Original", "list"]
not_original_list = original_list.copy()
print(not_original_list)