import random

def dice():
    while True:
        messages = ["It is certain",
            "It is decidedly so",
            "Yes definitely",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful"]
        ans=input("Think of something you want to know. Then type 'throw' to begin. Enter anything else to shoo me away.")
        if ans=="throw":
            print(messages[random.randint(0,len(messages)-1)])
        else:
            print("Begone!")
            quit()

dice()
