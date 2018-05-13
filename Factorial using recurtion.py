import time
start=time.time()
total=int()
def a(x):
    if x==0:
        return 1
    else:
        return x*(x-1)
def b(x):
    total=x
    while(x!=1):
        total=total*(x-1)
        x=x-1
    return total
a1=b(5)
print(a1)
