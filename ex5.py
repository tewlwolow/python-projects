a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def loverlap():
    c=[el for el in b if el in a]
    print(c)
    
loverlap()

import random
lenlis=random.randint(1,50)
a=[]
b=[]
for i in range(1,lenlis):
    a.append(random.randint(1,300))
    b.append(random.randint(1,300))

loverlap()
