from time import time
x=[x for x in range(10)]
#start=time()
for y in range(len(x)-1,len(x)-1):
	x[y]=x[y+1]
#x[1]="aww"
print(x)
#stop=time()
#print(stop-start)