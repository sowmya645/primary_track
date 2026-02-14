add=lambda a,b:a+b
print(add(5,3))
numbers=[1,2,3,4,5,6]
en=list(filter(lambda x:x%2==0,numbers))
print(en)
data=[{"name":"alice","age":30},
      {"name":"bob","age":20},
      {"name":"charles","age":25}]
yp=min(data,key=lambda x:x["age"]<30)
print(yp)