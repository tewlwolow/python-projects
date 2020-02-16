def palin():
    pal=input("Please write any word: ").lower()
    if pal[::-1]==pal:
        print("It's a palindrome.")
    else:
        print ("Whatever.")
        
palin()
