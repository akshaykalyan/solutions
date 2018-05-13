import math
def zeros(n):
    if n ==0:
    	return 0
    if len(str(n))==1:
        return 1
    var=100
    count=int()
    n=math.factorial(n)
    while True:
        if n%var==0:
            var*=100
            count+=2
        else:
            print(var,str(n))
            if(n%var)==0:
                if(n%(var//10))==0:
				    count+=1
                return count
print(zeros(30))
