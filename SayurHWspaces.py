value="abcdefg"
res=""

val=len(value)
cnt=0

for i in range(val):
    if cnt<3:
        res=res+value[i]
        cnt=cnt+1
    else:
        res=res+" "
        res=res+value[i]
        cnt=1
    
print(res)