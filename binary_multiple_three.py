import re
PATTERN = re.compile(r'^(0)*((0)*1(0(1)*0)*1)*(0)*$')
for x in range(100):
	print(re.match(PATTERN,"{:b}".format(x)))
	if x%3==0:
		print(True,x)

