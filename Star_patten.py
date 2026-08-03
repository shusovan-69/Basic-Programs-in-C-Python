for i in range(1,4):
    for j in range(1,4-i):
        print("",end="  ")
    for k in range(1,i+1):
        print("*",end=" ")
    for a in range (1,i):
        print("*",end=" ")
    print()
for l in range(1,3):
    for m in range(1,l+1):
        print("",end="  ")
    for n in range(1,4-l):
        print("*",end=" ")
    for s in range(1,3-l):
        print("*",end="")
    print()