# simple programme to check if a string is a palindrome
# includes check for case, removes spaces from input

from sys import exit


print('Welcome to Ultimate Palindrome Checker v 1.5. Type \'EXIT\' to exit.')

while True:
    var = str(input('Please provide any word. Case doesn\'t matter: '))
    var = var.replace(' ', '')
    if var == 'EXIT':
        exit()
    var = var.lower()
    if var[::-1] == var:
        print('The word provided is a palindrome.')
    else:
        print('The word provided is not a palindrome.')
