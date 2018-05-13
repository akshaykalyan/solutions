def has_unique_chars(str):
	str=str.lower()
	for x in xrange(len(str)):
		for y in xrange(x+1,len(str)):
			if str[x]==str[y]:
				return False
	return True
print(has_unique_chars("V\giKh_0,a5dk"))