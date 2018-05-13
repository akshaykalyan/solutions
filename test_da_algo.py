from time import time
x=[0]*10
a=time()
x.insert(0,"aww")
b=time()
print(b-a)
print(x)
x=[0]*10
a=time()
y=["aww"]
y.extend(x)
b=time()
print(b-a)
print(y)