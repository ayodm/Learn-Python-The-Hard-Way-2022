#Functions 

"""
What do functions do? 
1. name pieces of code the way variables name strings and numbers 
2. take arguments the way scripts take argv
3. Using 1 and 2 they let ou make your own mini-scripts or tiny commands

"""

# This one like the scripts with argv in the ex16,ex17
def print_two(*args): 
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Pointless but this shows we can just do this
def print_two_again(arg1, arg2): 
    print(f"arg1: {arg1}, arg2: {arg2}")


# Takes only one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# Takes no arguments
def print_none():
    print("I got nothing'.")

print_two("Ayo", "Mosanya")
print_two_again("Ayo2", "Mosanya2")
print_one("First!")
print_none()
