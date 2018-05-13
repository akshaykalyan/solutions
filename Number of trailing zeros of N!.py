import math
def zeros(n):
	maxmultipleoffive=1
	max5list=[]
	temp=[]
	t=[]
	while n>=maxmultipleoffive*5:
		maxmultipleoffive*=5
		max5list.append(maxmultipleoffive)
	for x in max5list:
		temp.append(n//x)
	temp=sorted(temp)
	t.append(temp[0])
	for x in range(len(temp)-1):
		t.append(temp[x+1]-temp[x])
	for x in range (len(t)):
		t[x]=t[x]*(len(t)-x)
	return sum(t)
print(zeros(1000))