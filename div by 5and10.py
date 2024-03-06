num=int(input("Enter a num: "))
sum=0

for i in range(0,num+1):
    if(i%5==0  and i%10==0 ):
        sum=sum+i
        
print(sum)