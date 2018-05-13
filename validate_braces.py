def validBraces(string):
    a="{[("
    b="}])"
    string=list(string)
    v=[]
    for x in string:
        if x in a:
            v.append(x)
        try:
            if x in b:
                if a.index(v.pop())!=b.index(x):
                    return False
        except:
            return False
    return v==[]
print(validBraces("()"))