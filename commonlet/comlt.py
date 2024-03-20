#commonletters
def sort(Wrd):
    sort_value=''.join(sorted(Wrd))
    sorted_string.append(sort_value)
    return sorted_string
   
   
string=["good","gode","doog","god","abc","cba"]
sorted_string=[]
count=0

for Wrd in string:
     sort(Wrd)
     
length=len(sorted_string)

for n in range(length):
    for j in range(n+1,length):
      if sorted_string[n] == sorted_string[j]:
        count+=1
    
print("common letters in Words and chrs: "+count)
