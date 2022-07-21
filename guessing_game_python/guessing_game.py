# Creating a guessing game using different basic tools we learned in Python so far
secret_word = "Tommy"
guess = ""


while guess != secret_word:
    guess = input("What is the secret word: ")
    print("That is the wrong answer, try again!")
print("Good job!")