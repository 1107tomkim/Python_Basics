# Creating a simple dictionary that converts 3 letter months to full months
# Make sure when creating a dictionary, state a name  =  to a {} followed by , to seperate
from calendar import month


monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

# You can print the accessed dictionary by using[key]
print(monthConversions["Nov"])
# You can also print the accessed dictionary by using the .get("key")
print(monthConversions.get("Dec"))
# You can set specific dictionary values for specific keys
print(monthConversions.get("Woop", "Not a valid key"))


# Dictionary can have both int and characters
monthConversions_number = {
    "1" : "January",
    "2" : "February",
    "3" : "March",
    "4" : "April",
    "5" : "May",
    "6" : "June",
    "7" : "July",
    "8" : "August",
    "9" : "September",
    "10" : "October",
    "11" : "November",
    "12" : "December"
}
print(monthConversions_number.get("1"))
print(monthConversions_number.get("2"))
print(monthConversions_number.get("3"))
print(monthConversions_number.get("4"))
print(monthConversions_number.get("5"))
print(monthConversions_number.get("6"))
