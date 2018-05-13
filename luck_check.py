def luck_check(string):
    temp1,temp2=0,0
    for x in range (len(string)//2):
        temp1+=int(string[x])
        temp2+=int(string[len(string)-1-x])
        print(temp1,temp2)
    if temp1==temp2:
        return True
    else:
        return False
print(luck_check('683179'))