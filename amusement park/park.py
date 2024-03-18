import datetime


def agee(dob):
    birth= datetime.datetime.strptime(dob,"%Y-%m-%d").date()
    today =datetime.date.today()
    age=today.year - birth.year
    return age
    
def ticket(age):
    a=50
    b=70
    if age >=18 :
        print(f"ADULT PRICE: {b}")
    elif age>=60:
        print(f"SENIOR PRICE: {a}")
    else:
        print(f"KID PRICE: {a}")
        
def discount(total_cost,day_of_Week):
    if day_of_Week =='Tuesday' and day_of_Week == 'thursday':
        dis_amt=0.8 * total_cost
        return dis_amt

def main(dis_amt,age):
    print("Welcome to the Amuesment Park")
    
    name =input("Enter your name: ")
    dob= input("Enter you birthday (YYYY-MM-DD) : ")
    agee(dob)
    print(f"Hi,{name}, Welcome!")
    print("Based on your age your ticket is calculated ")
    price=ticket(age)
    to_day=datetime.date.today()
    day_of_Week= to_day.strftime("%A")
    total_cost=price
    
    print(f"today is {day_of_Week}")
    discount(total_cost,day_of_Week)
    print(f"DISCOUNT AMOUNT for {day_of_Week} is: {dis_amt}")
    
    
    
if __name__ =='__main__':
    dis_amt=0
    age=0
    main(dis_amt,age)