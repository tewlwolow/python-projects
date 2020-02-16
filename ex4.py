def exfire():
    number=int(input("Give me something mathy: "))
    lis=list(range(1, number+1))
    lis=[div for div in lis if number%div==0]
    print(lis)
exfire()

