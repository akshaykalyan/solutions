def whoIsNext(r):
	n=1
	x=5
	t=5
	while (x<=r):
		n=n*2
		x=x+(n*5)
		t=5*n
	r=(r-(x-t))//n
	return r
print(whoIsNext(7))