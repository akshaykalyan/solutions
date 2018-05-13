import sys
import wrapper
s=[10 for x in range (1000000)]
t=""
sys.setrecursionlimit(10000000)
for x in range(100000):
    t+="10+"
t=t[:-1:]
@wrapper.epoch
def sum():
    global s
    sum(s)
@wrapper.epoch
def mult():
    1000*1000
@wrapper.epoch
def recursiveadd():
    global t
    eval(t)