def first():
    print("The first part is even/odd/4div checker. If you want to continue to the next part, type 'FROG'.")
    while True:
        try:
            usr_nmbr=input("Please write any number: ")
            if usr_nmbr=="FROG":
                break
            usr_nmbr=int(usr_nmbr)
            if usr_nmbr==0:
                print("You've typed void.")
            elif usr_nmbr%4==0:
                print("Your number is divisible by 4.")
            elif usr_nmbr%2==0:
                print("It's an even number!")
            else:
                print("It's not an even number!")
        except:
            print("Something went wrong.")
          
def second():
    from sys import exit as quitme
    print("Ok, now for something completely different. Type 'Let me out!' to quit.")
    if input()=="Let me out!":
        print("Programme finished.")
        quitme()
    while True:
        try:
            check=int(input("Please write any number you want divided: "))
            num=int(input("Please write any number to divide by: "))
            if check or num ==0:
                print("We don't use void here!")
            if check%num==0:
                print("It's divisible!")
            else:
                print("Oh, it's not divisible!")    
        except:
            print("Something went wrong.")
    
first()
second()
