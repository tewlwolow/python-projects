import sys

name=input("Write your name: ")
age=int(input("Write your age (use numbers): "))
for i in range(0,age):
    print(name+" will turn 100 in",str(2020+(100-age))+"."+"\n")
    
while True:
    terminal=input("Programme has finished. Type 'quit' and hit Enter to exit: ")
    if terminal=="quit":
        print("Finishing...")
        sys.exit()
    else:
        print("Error!")


