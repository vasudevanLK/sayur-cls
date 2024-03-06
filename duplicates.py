l=[1,2,3,4,4,5,5,6,7,8,8,9]
new=[]
dupli=[]

for i in l:
    if i not in new:
        new.append(i)
    else:
        dupli.append(i)
print(dupli)
      