x=1
def ap10(lists):
    if len(lists)==10:
        return lists
    else:
        if lists==[]:
            lists.append(1)
        lists.append(lists[-1]+1)
        ap10(lists)
ls=[]
ap10(ls)
print(ls)
