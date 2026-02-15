import re
lis=[False,False,False,False,False]
password=input("enter your password")

if re.search(r'[A-Z]',password):
    lis[0]=True
if re.search(r'[a-z]',password):
    lis[1]=True
if re.search(r'[0-9]',password):
    lis[2]=True
if re.search(r'[^a-zA-Z0-9]',password):
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