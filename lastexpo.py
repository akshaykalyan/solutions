def last_digit(n1, n2):
	if n2==0:
		return 1
	n1=int(str(n1)[-1])
	if n1 in (1,5,6,0):
	    return n1
	elif n1 == 4:
	    return [6,4][n2%2]
	elif n1 == 9:
	    return [1,9][n2%2]
	elif n1 == 2:
		return[6,2,4,8][n2%4]
	elif n1 == 3:
		return[1,3,9,7][n2%4]
	elif n1 == 7:
		return[1,7,9,3][n2%4]
	else:
		return[6,8,4,2][n2%4]
print(last_digit(222, 5))