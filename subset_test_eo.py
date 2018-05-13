import itertools
def subsets_parity(n,k):
    return  len(set(itertools.combinations([x for x in range(n)],k)))%2
aww=40
for x in range(1,aww):
	print(subsets_parity(aww,x),x)