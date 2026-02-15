try:
    a=eval(input("enter numerator: "))
    b=eval(input("enter denominator: "))
    re=a/bprint("result",re)
except Exception as e:
    print("error:Division by zero is not allowed")
finally:
    print("execution completed.")