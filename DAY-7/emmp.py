def designation(func):
    def wrapper(desi,num):
        print("designation: ",desi)
        return func(desi,num)
    return wrapper
def salary(func):
    def wrapper(desi,num):
        print("Salary:",num)
        return func(desi,num)
    return wrapper
@designation
@salary
def emp_info(desi,num):
    return f"{desi},{num}"
emp_info("HR",600)