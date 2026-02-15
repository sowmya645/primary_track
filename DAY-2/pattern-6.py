a=eval(input("enter a number"))
for i in range (0,a):
    for j in range (a-i):
        print(" ",end="")
    for j in range (i+1):
        print(i," ",end="")
    for j in range (i+1,a-i):
        print(" ",end="")
    print()