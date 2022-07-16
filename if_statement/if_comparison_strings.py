# String comparing using the if statement.

def match_string(string1, string2, string3): # Function to compare strings
    if string1 == string2 or string1 == string3: # Checking to see if String1 matches with either string2 or string3
        return string1 # If so then there is a match and therefore it will print out string1
    else: # else meaning there are no matching strings at all
        print("There is not matching string") # It will print out the statement.

print(match_string("Bat", "bat", "Bet"))