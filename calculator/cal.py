def add(a,b):
    output=a+b
    print(f"addition of {a} + {b} is: {output}")
    
def sub(a,b):
    output=a-b
    print(output)
    print(f"Subraction of {a} + {b} is: {output}")
    
def mul(a,b):
    output=a*b
    print(output)
    print(f"Multiple of {a} + {b} is: {output}")
    
def div(a,b):
    if b ==0:
        print("ERROR cant divide")
    else:   
        output=a/b
        print(output)
        print(f"DIvision of {a} / {b} is: {output}")

def main():
    print("CALCULATOR")
    while True:
     val1=int(input("Enter a num"))
     val2=int(input("enter a num"))
     print("/n SELECT OPERATOR:")
     print('1. +')
     print('2. -')
     print('3. *')
     print('4. /')
     
     choose= int(input('select: (1-4)'))
     
     if choose == 1:
        add(val1,val2)
     elif choose ==2:
        sub(val1,val2)
     elif choose ==3:
        mul(val1,val2)
     elif choose ==4:
        div(val1,val2)
    
if __name__ =='__main__':
    main()