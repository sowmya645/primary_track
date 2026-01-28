a=eval(input("enter a number"))
for i in range (0,a):
    for j in range (0,a):
        if(i+j==a-1 or i==0 or i==a-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
