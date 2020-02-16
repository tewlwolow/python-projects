catNames=[]
while True:
    print("Enter the name of cat "+str(len(catNames)+1)+" (or enter nothing to stop and print the names.):")
    name=input()
    if name=="":
        break
    catNames=catNames+[name]
print("The cat names are:")
for name in catNames:
    print("  "+name)
print("And now cats in a box:",str(catNames)+"!")
