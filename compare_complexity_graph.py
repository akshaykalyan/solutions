def matplot():
	import matplotlib.pyplot as plt
	from sys import getsizeof
	from array import array
	from math import log
	r=65536

	prev=0
	x3 = [x for x in range(r)]
	y3 = []
	t3=array("H",[])
	for x in range(r):
		t3.append(0)
		y3.append(getsizeof(t3))
	plt.plot(x3, y3, label = "list")

	
	x4 = [x for x in range(r)]
	y4 = array("I",[])
	t4=[]
	for x in range(r):
		y4.append(1)
		t4.append(getsizeof(y4))
	plt.plot(x4, t4, label = "carray")
	


	# naming the x axis
	plt.xlabel('input')
	# naming the y axis
	plt.ylabel('size')
	# giving a title to my graph
	plt.title("list vs carray(unsigned short int )")
	 
	# show a legend on the plot
	plt.legend()
	plt.grid(True)
	# function to show the plot
	plt.show()

matplot()