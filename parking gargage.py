from datetime import datetime, timedelta

def initial():
    print("YOUR PARKING AREA")
    print("__________________")
    slot = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    for i in range(len(slot)):
        for j in range(len(slot[0])):
            print(slot[i][j],end='')
        print()
    available = 3 * 3
    toll_coll = 0
    
    print("_________________")
    return slot, available, toll_coll

    
def enter_parking(slot,available):
    car_id=0
    count = 0
    for i in range(len(slot)):
        for j in range(len(slot[i])):
            if slot[i][j] == 0:
                count += 1
    if count == 0:
        print("All SLOTS are full ")
    else:
        for i in range(len(slot)):
            for j in range(len(slot[i])):
                if slot[i][j] == 0:
                    print(f"Car Parked at Spot {i + 1}-{j + 1}")
                    entry_time =datetime.now()
                    slot[i][j] = 1  # corrected assignment operator
                    car_id = f"{i + 1}-{j + 1}"
                    print(f"Your Car id {car_id}")
                    return car_id, entry_time  # corrected assignment of entry_time
                    
def time_calc(entry_time,toll_fee,toll_coll):
    toll_fee = 100
    exit_time=datetime.now()
    difference = exit_time - entry_time 
    hrs=input("enter your parking hours: ")
    if hrs < difference:
         toll_coll += toll_fee
         toll_coll,toll_fee
         
    if difference > timedelta(hours=2):
        print("_________________")
        print(f"Late Parking Fee:  Rs.{150} per hour")
        toll_coll= 20
        toll_coll += toll_fee
        return toll_fee,toll_coll

        

def leave_parking(toll_coll, car_id,entry_time):
    if car_id != 0:
        time_calc(entry_time,toll_fee,toll_coll)  # corrected function call, passing entry_time
        print("------------------")
        print(f"Car left at {car_id} , Toll Collection: {toll_fee}")  
        print("------------------")
        return toll_coll, toll_fee ,entry_time 
    else:
        print("------------------")
        print("NO car found to Exit from parking ! ")
        print("------------------")
        return toll_fee  ,entry_time

def Tollamt(toll_coll):
    val = str(input("Are you Willing to donate (Y/N): ")).upper()
    if val == 'Y':
        donate_amt = 0
        print("____________________")
        print("Your help makes a difference to save lives ")
        amt = float(input("Donation Amount: "))
        donate_amt += amt
        print(f"Your Donation amount: {donate_amt}")
        print("____________________")
    else:
        print("--------------------")
        print(f"Your Total Collection on toll: {toll_coll}")


# Main program
slot, available, toll_coll = initial()
car_id = None  # initializing car_id
toll_fee=100
hrs=0

while True:
    print("------- CAR PARKING APPLICATION---------")
    print("\nMenu:")
    print("1. Initialize Parking")
    print("2. Enter Parking")
    print("3. Leave Parking")
    print("4. Check Toll Amount")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        slot, available, toll_coll = initial()
        
    elif choice == 2:
        car_id, entry_time = enter_parking(slot, available)  
        
    elif choice == 3:
         toll_coll, toll_fee, entry_time = leave_parking(toll_coll, car_id, entry_time) 
        
    elif choice == 4:
        Tollamt(toll_coll)
        
    elif choice ==5:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")
