a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def printer():
    for e in a:
        if e<5:
            print(e)

def newlister():
    l=[]
    for e in a:
        if e<5:
            l.append(e)
    print(l)

def newlister_cons():
    print([e for e in a if e<5])

def useri():
    u=int(input("Write any number: "))
    print([e for e in a if e<u])
    
printer()
newlister()
newlister_cons()
useri()

a.extend([34,546,98778,0,34,0,2313,-1])

printer()
newlister()
newlister_cons()
useri()




