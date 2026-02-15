
bill=eval(input("enter bill amount")) #1000 above
day=input("enter day:")#saturday or sunday
membership=input("enter membership:")
if(bill>1000 and "GOLD" in membership ):
    if("SATURDAY" in day or "SUNDAY" in day):
        print("you have got 20% discount in bill")