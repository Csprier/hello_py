# Create a program that can take in input of the users name
# save the name in a variable
# pass the variable through a function and print "Hello ________"

name = input("What's your name? ")
def hello(name):
    print(f"Hello {name}. o/")

hello(name)