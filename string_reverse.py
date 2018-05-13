def reverse(x):
    x=x.split()
    tmp=""
    for i in range(len(x)):
        tmp=tmp+" "+x[len(x)-i-1]
    return tmp[1:len(tmp)]

print(reverse('Hello World'))
