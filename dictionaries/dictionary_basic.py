# Creating a simple dictionary that converts 3 letter months to full months
# Make sure when creating a dictionary, state a name  =  to a {} followed by , to seperate
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