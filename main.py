#Function for input name
def input_name():
    return input("Your name ")

#Function for asking how are you (with name variable)
def how_are_you(name):
    print(f"Are you OK, {name}?")
    if input() in ('Yes', 'yes'):
        print("That's cool!")
    else:
        print("Don't worry :)")

#Main part
name1 = input_name()
print(f"Hello, {name1}")
how_are_you(name1)