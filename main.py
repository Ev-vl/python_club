def input_name():
    return input("Your name ")

def how_are_you(name):
    print(f"Are you OK, {name}?")
    if input() in ('Yes', 'yes'):
        print("That's cool!")
    else:
        print("Don't worry :)")

name1 = input_name()
print(f"Hello, {name1}")
how_are_you(name1)