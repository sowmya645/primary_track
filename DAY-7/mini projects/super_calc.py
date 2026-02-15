def get_operator():
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.division")
    print("5.square root")
    
    a=eval(input())
    b=input("enter operator:") 
    c=eval(input())
    if(b=='+'):
        print(a+c)
    elif(b=='-'):
        print(a-c)
    elif(b=='*'):
        print(a*c)
    elif(b=='/'):
        print(a/c)
    elif(b=='%'):
        print(a%c)
            