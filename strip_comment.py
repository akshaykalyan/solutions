import re
def solution(string,markers):
    string=string.split("\n")
    c=[]
    for x in string:
        for y in markers:
            t=re.search("("+y+").*",x)
            
            if t!=None:
                t=t.group(0)
                print(t)
                x=x.rstrip(t)
                print(x)
                x=x.rstrip(" ")
        c.append(x)
    return "\n".join(c)
solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
