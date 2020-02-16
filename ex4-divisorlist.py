def exfire():
    while True:
        try:
            number=int(input("Give me any number, and I shall show you its divisors: "))
            lis=list(range(1, number+1))
            lis=[div for div in lis if number%div==0]
            print(lis)
        except:
            print("Try again!")
exfire()
