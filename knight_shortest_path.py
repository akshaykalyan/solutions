from math import floor,log
def position_generator(position):
	if position==None:
		return [None]*8
	x_dir={"a","b","c","d","e","f","g","h"}
	y_dir={"1","2","3","4","5","6","7","8"}
	result=[]
	pos_x=ord(position[0])
	pos_y=int(position[1])
	result.append(chr(pos_x+1)+str(pos_y+2))
	result.append(chr(pos_x-1)+str(pos_y-2))
	result.append(chr(pos_x+1)+str(pos_y-2))
	result.append(chr(pos_x-1)+str(pos_y+2))
	result.append(chr(pos_x+2)+str(pos_y+1))
	result.append(chr(pos_x-2)+str(pos_y-1))
	result.append(chr(pos_x+2)+str(pos_y-1))
	result.append(chr(pos_x-2)+str(pos_y+1))
	
	for x in range(8):
		if len(result[x])==3 or result[x][0] not in x_dir or result[x][1] not in y_dir:
			result[x]=None
	return result
	
def knight(p1, p2):
	if p1==p2:
		return 0
	pos_list=[p1]
	cursor=0
	t=0
	count=1
	while(t==0):
		for x in position_generator(pos_list[cursor]):
			pos_list.append(x)
			count+=1
			if x==p2:
				return floor (log(count*7,8))
		cursor+=1

print(knight("a1","h8"))