
#this program checks the word occurance in nxt to same Word eg: " the word the the occurs one time  " output: 1

filepath='Wordoccurance\demo.txt'

with open(filepath,'r') as file:
    
    txtfile=file.read().lower()
    textfile=txtfile.replace('.',' ')
    words=textfile.split(' ')
    
    pre=''
    
    count=0
    cnt=0
    for i in range(len(words)):
        if pre == words[i]:
            count+=1
            cnt=cnt+1
            if cnt==1:
              print(f'Word: {words[i]}')
                
        else:
            pre=words[i]
            
    
    print(f' count: {count}')