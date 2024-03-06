ro=str(input("enter input: "))
n=3
r=ro.upper()
r=len(r)
for i in range(n+1):
    for j in range(i):
        print(ro[j],end=" ")
    print("\n")