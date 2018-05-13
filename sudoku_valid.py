def validSolution(board):
	valid={1,2,3,4,5,6,7,8,9}
	for a in range(9):
		temp=[]

		for c in range(9):
			temp.append(board[a][c])
		if set(temp)!=valid:
			return False

	for a in range(9):
		temp=[]
		for c in range(9):
			temp.append(board[c][a])
		if set(temp)!=valid:
			return False

	for a in range(0,27,3):
		temp=[]
		for x in range(9):
			temp.append(board[((a//9)*3)+(x//3)][(a%9)+x%3])
		if set(temp)!=valid:
			return False
	return True
print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                         [6, 7, 2, 1, 9, 0, 3, 4, 9],
                         [1, 0, 0, 3, 4, 2, 5, 6, 0],
                         [8, 5, 9, 7, 6, 1, 0, 2, 0],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 0, 1, 5, 3, 7, 2, 1, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 0, 0, 4, 8, 1, 1, 7, 9]]))