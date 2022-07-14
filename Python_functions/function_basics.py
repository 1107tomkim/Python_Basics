# Creating a simple function

def sayhi():
    print("Hello User")

# Calling the simple function
sayhi()


# Creating a function with parameters
# Parameters are elements that we are providing as input
def addit(a, b):
    c = a + b
    print(c)
addit(2, 5)
addit(3, 6)


# Creating a function with multiple inputs
def say_hi(name, age):
    print("Hello " + name + " " + "you are " + age + " years old!")

say_hi("Mike", "10")
say_hi("Steve", "20")
