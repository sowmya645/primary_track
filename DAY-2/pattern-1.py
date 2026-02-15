a=eval(input("enter size of rectangle"))
for i in range (0,a):
    for j in range (0,a):
        if(i==a-1 or j==0 or j==a-1 or i==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()

            
        
            