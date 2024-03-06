def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return 1
        
    print('not present')
l=[1,2,3,4,5,6,7,8,9]
search(l,6)