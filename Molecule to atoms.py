import string
import re
def parse_molecule (formula):
	a="{[("
	b="}])"
	loop=0
	pros=[]
	length=len(formula)
	stack=[]
	d={}
	while(loop<length):
		if formula[loop] in string.ascii_uppercase:
			if loop+1<length and formula[loop+1] in string.ascii_lowercase :
				if loop+2<length and formula[loop+2].isdigit() :
					pros.append([formula[loop]+formula[loop+1],int(re.search(r"^\d*",formula[loop+2:]).group(0))])
					loop+=2+len(re.search(r"^\d*",formula[loop+2:]).group(0))
				else:
					pros.append([formula[loop]+formula[loop+1],1])
					loop+=2
			elif loop+1<length and formula[loop+1].isdigit():
				pros.append([formula[loop],int(re.search(r"^\d*",formula[loop+1:]).group(0))])
				loop+=1+len(re.search(r"^\d*",formula[loop+1:]).group(0))
			else:
				pros.append([formula[loop],1])
				loop+=1
		
		elif formula[loop] in a:
			pros.append([formula[loop]])
			loop+=1

		elif formula[loop] in b:
			if loop+1<length and formula[loop+1].isdigit():
				pros.append([formula[loop],int(re.search(r"^\d*",formula[loop+1]).group(0))])
				loop+=1+len(re.search(r"^\d*",formula[loop+1]).group(0))
			else:
				pros.append([formula[loop],1])
				loop+=1
	r=[]
	for x in pros[::-1]:
		if x[0] in b:
			if stack==[]:
				stack.append(x)
			else:
				x[1]=x[1]*stack[-1][1]
				stack.append(x)
		elif x[0] in a:
			stack.pop()
		elif x[0].isalpha():
			if stack!=[]:
				x[1]=x[1]*stack[-1][1]
		r.append(x)
	for x in r:
		if x[0].isalpha():
			d[x[0]]=0
	for x in r:
		if x[0].isalpha():
			d[x[0]]=d[x[0]]+x[1]
	return d
