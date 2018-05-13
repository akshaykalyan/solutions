def snail(a):
	if a==[[]]:
		return []
	looprun=int(len(a)/2) if len(a)%2==0 else (len(a)//2)+1 
	res=[]
	for loopno in range(looprun):
		for i in range(len(a)-2*loopno):
			res.append(a[loopno][i+loopno])
		for j in range((len(a)-1)-2*loopno):
			res.append(a[1+j+loopno][(len(a)-1)-loopno])
		for j in range((len(a)-1)-2*loopno):
			res.append(a[(len(a)-1)-loopno][(len(a)-2)-loopno-j])
		for k in range((len(a)-2)-(loopno*2)):
			res.append(a[len(a)-2-k-loopno][loopno])
	return(res)