# Creating a guessing game using different basic tools we learned in Python so far
secret_word = "Tommy"
guess = ""
count = 0
count_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if count < count_limit:
        guess = input("What is the secret word: ")
        print("That is the wrong answer, try again!")
        count += 1
    else:
        out_of_guesses = True
        print("You are out of guesses")

if out_of_guesses:
    print("Nice try but no cookie!")
else:
    print("You win!")