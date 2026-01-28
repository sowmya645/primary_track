# recharge=eval(input("enter recharge amount"))
# databalance=eval(input("enter data balance in gb"))
# if(recharge>=399 and databalance>=2):
#     print("additional bonus of 2gb data is given")
# else:
#     print("no bonus")

# bill=eval(input("enter bill amount")) #1000 above
# day=input("enter day:")#saturday or sunday
# membership=input("enter membership:")
# if(bill>1000 and "GOLD" in membership ):
#     if("SATURDAY" in day or "SUNDAY" in day):
#         print("you have got 20% discount in bill")

# for i in range (1,5):
#     password=eval(input("enter crct passowrd"))
#     user=input("enter username")
#     if(i==4): 
#         print("all attempts failed")
#         break
#     if(password==123 and user=="admin"):
#         print("crct")
#         break
#     else:
#         print(f"you have {4-i} attempts")
        
        
lis=[]
while True:
    res=input("enter ")
    if(res=="done"):
        print(lis)
        break
    else:
        lis.append(res)
