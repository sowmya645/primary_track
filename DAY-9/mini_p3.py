import numpy as np
a=np.arange(1,25)
b=a.reshape(2,3,4)
filter_arr=b[b>10]
print("elements greater than 10")
print(filter_arr)
print("number of elements that are even")
en=b[b%2==0]
cen=len(en)
print(cen)
h=b
h[h<10]=0
print("elements less than 10 replacing with 0")
print(h)