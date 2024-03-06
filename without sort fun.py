l=[1,2,3,4,5,6,7,8,9]
nl=[]
while l:
    min=l[0]
    for x in l:
        if x < min:
         min= x
    nl.append(min)
    l.remove(min)
print(nl)