import random

def roll():
    return random.randint(1,6)

def points(roll):
    if roll==1:
        return 1
    elif roll==2:
        return 5
    elif roll==3:
        return 15
    elif roll==4:
        return -5
    elif roll==5:
        return -15
    elif roll==6:
        return -1
    
def play():
    User=0
    bot=0
    rolls=0
    
    while True:
        rolls+=1
        spin=roll()
        User+= points(spin)
        if User ==100:
         x=print(f"Rolls: {rolls} , Score: {User}")
         y=print("User Wins...")
         return x,y
           
        
        rolls+=1       
        spin=roll()
        bot+= points(spin)
        if bot == 100:
         x=print(f"Rolls: {rolls} , Score: {User}")
         y=print("bot Wins...")
         return x,y
       


while True:    
    input("Enter to play game:")
    play()    