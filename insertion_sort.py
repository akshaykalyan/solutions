a=[2,3,1,4,8,5,10,0]
for x in xrange(1,len(a)):
	cur=a[x]
	tmp=x
	while (tmp>0 and cur[tmp-1]>cur[tmp]):
		cur[tmp-1],cur[tmp]=cur[tmp],cur[tmp-1]
		tmp-=1
print(cur)