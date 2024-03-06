#remove duplicates

new=''
dupli=[]
value= input("enter your input: ")

for i in value:
    if i not in new:
        new+=i
    else:
        dupli+=i
        
print(f"removed duplicated words: ",new)
    