def sudoku(puzzle):
	mark=0
	puzzle= [[[t for t in range(1,10)] if i==0 else [i] for i in x] for x in puzzle]
	for a in range (9):
		for b in range(9):##set conversion
			puzzle[a][b]=set(puzzle[a][b])
	# loop=True
	while mark!=20 :
	# while loop==True:
		for a in range (9):#horizontal minus
			temp1=set()
			for c in range(9):##create set of right value
				if len(puzzle[a][c])==1:
					temp1.add(list(puzzle[a][c])[0])
			for c in range(9):
				if len(puzzle[a][c])!=1:
					puzzle[a][c]-=temp1
		for a in range (9):#verticle minus
			temp2=set()
			for c in range(9):
				if len(puzzle[c][a])==1:
					temp2.add(list(puzzle[c][a])[0])
			for c in range(9):
				if len(puzzle[c][a])!=1:
					puzzle[c][a]-=temp2
		for a in range(0,27,3):#box minus
			temp3=set()
			for x in range(9):
				if len(puzzle[((a//9)*3)+(x//3)][(a%9)+x%3])==1:
					temp3.add(list(puzzle[((a//9)*3)+(x//3)][(a%9)+x%3])[0])
			for x in range(9):
				if len(puzzle[((a//9)*3)+(x//3)][(a%9)+x%3])!=1:
					puzzle[((a//9)*3)+(x//3)][(a%9)+x%3]-=temp3
		#unique cut horizontal
		for a in range (9):
			for j in range(1,10):
				cnt =0
				mr=0
				q=0
				for b in range(9):
					if j in puzzle[a][b]:
						cnt+=1
						mr=q
					if b==8 and cnt==1:
						puzzle[a][mr]=set([j])
					q+=1
		#unique cut verticle
		for a in range (9):
			for j in range(1,10):
				cnt =0
				mr=0
				for b in range(9):
					if j in puzzle[b][a]:
						cnt+=1
						mr=b
					if b==8 and cnt==1:
						puzzle[mr][a]=set([j])
		#unique box cut
		for a in range (0,27,3):
			for j in range(1,10):
				cnt =0
				mr=0
				cr=0
				for x in range(9):
					if j in puzzle[((a//9)*3)+(x//3)][(a%9)+x%3]:
						cnt+=1
						mr=(a%9)+x%3
						cr=((a//9)*3)+(x//3)
					if x==8 and cnt==1:
						puzzle[cr][mr]=set([j])

		for a in range (9):#horizontal minus
			for b in range(9):
				if puzzle[a].count(puzzle[a][b])==len(puzzle[a][b]):
					for c in range(9):
						if puzzle[a][b]!=puzzle[a][c]:
							puzzle[a][c]-=puzzle[a][b]

		for a in range (9):#verticle pair minus
			temp=[]
			for b in range(9):
				temp.append(puzzle[b][a])
			for b in range(9):
				if temp.count(puzzle[b][a])==len(puzzle[b][a]):
					for c in range(9):
						if puzzle[b][a]!=puzzle[c][a]:
							puzzle[c][a]-=puzzle[b][a]
		for a in range(0,27,3):#box minus pair
			temp3=[]
			for x in range(9):
				temp3.append(puzzle[((a//9)*3)+(x//3)][(a%9)+x%3])
			for  x in range(9):
				if temp3.count(puzzle[((a//9)*3)+(x//3)][(a%9)+x%3])==len(puzzle[((a//9)*3)+(x//3)][(a%9)+x%3]):
					for c in range(9):
						if puzzle[((a//9)*3)+(x//3)][(a%9)+x%3]!=puzzle[((a//9)*3)+(c//3)][(a%9)+c%3]:
							puzzle[((a//9)*3)+(c//3)][(a%9)+c%3]-=puzzle[((a//9)*3)+(x//3)][(a%9)+x%3]


		# print()
		# for x in puzzle:
		# 	print(x)


		pair=[]
		for a in range(0,27,3):#box minus pair
			temp3=[]
			for x in range(9):
				i=((a//9)*3)+(x//3)
				j=(a%9)+x%3
				temp3.append(puzzle[i][j])
			for t in range(1,10):
				if str(temp3).count(str(t)) in (2,3):
					inde=[]
					for c in range(9):
						i=((a//9)*3)+(c//3)
						j=(a%9)+c%3
						if t in temp3[c]:
							inde.append([i,j,t])
					pair.append(inde)
		for x in pair:
			r=[]
			if len(x)==3 and x[0][0]==x[1][0]==x[2][0]:
				if x[0][1] in (0,1,2):
					r=[3,4,5,6,7,8]
				elif x[0][1] in (3,4,5):
					r=[0,1,2,6,7,8]
				else:
					r=[0,1,2,3,4,5]
			for i in r:
				puzzle[x[0][0]][i]-=set([x[0][2]])
			if len(x)==2 and x[0][0]==x[1][0]:
				if x[0][1] in (0,1,2):
					r=[3,4,5,6,7,8]
				elif x[0][1] in (3,4,5):
					r=[0,1,2,6,7,8]
				else:
					r=[0,1,2,3,4,5]
			for i in r:
				puzzle[x[0][0]][i]-=set([x[0][2]])


			

			r=[]
			if len(x)==3 and x[0][1]==x[1][1]==x[2][1]:
				if x[0][0] in (0,1,2):
					r=[3,4,5,6,7,8]
				elif x[0][0] in (3,4,5):
					r=[0,1,2,6,7,8]
				else:
					r=[0,1,2,3,4,5]
			for i in r:
				puzzle[i][x[0][1]]-=set([x[0][2]])
			if len(x)==2 and x[0][1]==x[1][1]:
				if x[0][0] in (0,1,2):
					r=[3,4,5,6,7,8]
				elif x[0][0] in (3,4,5):
					r=[0,1,2,6,7,8]
				else:
					r=[0,1,2,3,4,5]
			for i in r:
				puzzle[i][x[0][1]]-=set([x[0][2]])

		# print()
		# for x in puzzle:
		# 	print(x)







		# loop=False
		# for x in range(9):#validate
		# 	for y in range(9):
		# 		if len(puzzle[x][y])!=1:
		# 			loop=True
		# if loop==False:
		# 	for x in range(9):
		# 		for y in range(9):
		# 			puzzle[x][y]=list(puzzle[x][y])[0]
		mark+=1

	print()
	for x in puzzle:
		print(x)

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]



# puzzle = [[8,0,0,0,0,0,0,0,0],
#           [0,0,3,6,0,0,0,0,0],
#           [0,7,0,0,9,0,2,0,0],
#           [0,5,0,0,0,7,0,0,0],
#           [0,0,0,0,4,5,7,0,0],
#           [0,0,0,1,0,0,0,3,0],
#           [0,0,1,0,0,0,0,6,8],
#           [0,0,8,5,0,0,0,1,0],
#           [0,9,0,0,0,0,4,0,0]]

# puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8], 
#           [0, 8, 0, 0, 9, 0, 0, 3, 0], 
#           [2, 0, 0, 0, 0, 5, 4, 0, 0], 
#           [4, 0, 0, 0, 0, 1, 8, 0, 0], 
#           [0, 3, 0, 0, 7, 0, 0, 4, 0], 
#           [0, 0, 7, 9, 0, 0, 0, 0, 3], 
#           [0, 0, 8, 4, 0, 0, 0, 0, 6], 
#           [0, 2, 0, 0, 5, 0, 0, 8, 0], 
#           [1, 0, 0, 0, 0, 2, 5, 0, 0]]


# puzzle = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
#  [0, 0, 0, 4, 0, 6, 0, 0, 0],
#  [0, 0, 5, 0, 7, 0, 3, 0, 0],
#  [0, 6, 0, 0, 0, 0, 0, 4, 0],
#  [4, 0, 1, 0, 6, 0, 5, 0, 8],
#  [0, 9, 0, 0, 0, 0, 0, 2, 0],
#  [0, 0, 7, 0, 3, 0, 2, 0, 0],
#  [0, 0, 0, 7, 0, 5, 0, 0, 0],
#  [1, 0, 0, 0, 4, 0, 0, 0, 7]]

sudoku(puzzle)