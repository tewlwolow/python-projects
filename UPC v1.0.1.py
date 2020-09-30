import sys

print("Welcome to the Ultimate Palindrome Checker v 1.0.1. Type 'EXIT' to exit.")

while True:
    var = str(input("Please provide any word. Case doesn't matter: "))
    if var == "EXIT":
        sys.exit()
    elif var[::-1].lower() == var.lower():
        print("The word provided is a palindrome.")
    else:
        print("The word provided is not a palindrome.")