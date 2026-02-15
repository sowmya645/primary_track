lis=[False,False,False,False,False]
password=input("enter your password")
for c in password:
    if c.islower():
        lis[0]=True
    if c.isupper():
        lis[1]=True
    if c.isdigit():
        lis[2]=True
    if not c.isalnum():
        lis[3]=True
    if len(password)>=8:
        lis[4]=True
j=0
for i in lis:
    if i==False:
        print("poor")
        j=1
        break
if(j!=1):
    print("strong")
    