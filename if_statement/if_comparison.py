# Comparing numbers using the if statement

# Function to check which 3 number is the highest
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # Checks to see if number 1 is bigger or equal to num2 and num3. 
        return num1
    elif num2 >= num1 and num2 >= num3: # Checks to see if number 2 is bigger or equal to num1 and num2.
        return num2
    else: # If none of those conditions above are true then print num3 as the max value.
        return num3


print(max_num(3,4,5))
