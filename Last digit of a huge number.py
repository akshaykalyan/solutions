def eval(a):
	count=0
	ch=0
	lis=[]
	for x in a:
		if x!=0:
			if ch==0:
				lis.append(x)
			else:
				break
		else:
			count+=1
			ch=1
	if ch==0:
		return a
	if count%2==1:
		lis.append(0)
	else:
		lis.append(1)
	return lis
def last_digit(lst):
	if lst==[]:
		return 1
	lst=eval(lst)
	if len(lst)==1:
		return lst[0]%10
	elif lst[1]==0:
		return 1
	elif lst[0]==0:
		return 0
	elif len(lst)==2:
		return(pow(lst[0],lst[1],10))
	rules={0:[0,0,0,0],
		1:[1,1,1,1],
		2:[6,2,4,8],
		3:[1,3,9,7],
		4:[6,4,6,4],
		5:[5,5,5,5],
		6:[6,6,6,6],
		7:[1,7,9,3],
		8:[6,8,4,2],
		9:[1,9,1,9],
		0:[0,0,0,0]}
	l=lst[1:]
	t=lst[-1]
	for x in range(len(l)-1):
		t=pow(l[len(l)-1-1-x],t,4)
		if t==0 and lst[-1-x]!=0:
			t=4
		if t==1 and lst[-1-x]!=0 and lst[-1-x]!=1:
			t=5
	return rules[lst[0]%10][t%4]
print(last_digit([2, 2, 2, 0]))