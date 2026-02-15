# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("before the function call")
#         result=func(*args)
#         print("after")
#         return result
#     return wrapper
# @decorator
# def add(a,b):
#     return a+b
# print(add(2,3)) 
def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            
            for _ in range(n):
                result=func(*args,**kwargs)
            
            return result
        return wrapper
    return decorator
@repeat(10)
def greet():
    print("hi")
greet()