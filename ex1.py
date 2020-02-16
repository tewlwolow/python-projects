import sys

name=input("Skriv inn namnet ditt: ")
age=int(input("Skriv inn alderen din (bruk tal, ikkje ord): "))
years=int(input("Skriv inn eit anna tal: "))
for i in range(0,years):
    print(name+" skal vera 100 år gamal i",str(2020+(100-age))+"."+"\n")
    
while True:
    terminal=input("Programmet har avslutta. Tast inn 'quit' og slå Enter for å slutte: ")
    if terminal=="quit":
        print("Sluttar.")
        sys.exit()
    else:
        print("Hæ?")


