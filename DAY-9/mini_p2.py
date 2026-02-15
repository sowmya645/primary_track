import numpy as np
c=np.arange(1,25).reshape(2,3,4)
print(c)
b=c
print(b)
print()
print("first row of all layers ")
a=b[0:2,0,]
print(a)
print("last layer")
print(b[-1])
print("layer=1,row=2,column=3")
print(b[0,1,2])
print("first layer")
print(b[0])
print("last row of all layers")
print(b[0:2,-1,])
print("first coloumn of all layers")
print(b[0:2,:,0])