import sys
data=[]
n=input()
n=int(n)
for x in range(n):
	print(len(data),sys.getsizeof(data),data)
	data.append(None)

for x in range (n):
	data.pop()
	print(len(data),sys.getsizeof(data),data)
	
