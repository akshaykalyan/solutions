arr = [345, 32, 45]
t=[]
main=[]
for x in arr:
	if t==[] or t[-1]<x:
		t.append(x)
	else:
 		main.append(t)
 		t=[x]
main.append(t)
t=[len(x) for x in main ]
t=t.index(max(t))
print(main[t] if len(main[t])>2 else "No increasing subsequence")