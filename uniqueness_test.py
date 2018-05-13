x= [1,4,2,3,9,3,6,1]
for a in range(len(x)):
    for b in range(a+1,len(x)):
        print(x[a],x[b])
        if x[a]==x[b]:
            print(False)
    
