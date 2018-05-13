from time import time
def epoch(some_func):
	x=time()
	some_func()
	print(time()-x)