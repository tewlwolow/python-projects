def collatz():
    import sys
    print ("Ten program służy do generowania sekwencji Collatza. Wpisz 'Koniec', aby zakończyć program.")
    while True:
        try:
            number=input("Wprowadź dowolną liczbę całkowitą: ")
            if number=="Koniec":
                print("Program zakończył pracę.")
                sys.exit()
            number=int(number)
            while number!=1:
                if number%2==0:
                    print(number)
                    number=number//2
                elif number%2==1:
                    print(number)
                    number=(3*number)+1
            if number==1:
                print(number)
        except ValueError:
            print("Wystąpił błąd. Proszę użyć liczb całkowitych.")
   
collatz()
