from time import time
n=input()
a=[None]
b=[]
start= time()
for x in range(n//2):
	a.append(None)
	a.pop()
stop=time()
print("ocilations at memory allocation and deallocation")
print(stop-start)
start= time()
for x in range(n):
	b.append(None)
stop=time()
print("Dynamic allocation")
print(stop-start)
