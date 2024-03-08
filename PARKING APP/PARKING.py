def initial():
    print("YOUR PARKING AREA")
    print("------------------")
    slot = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    available = 3 * 3
    toll_coll = 0
    print(slot)
    print("------------------")
    return slot, available, toll_coll


def enter_parking(slot, available):
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
                    slot[i][j]==1
                    car_id = f"{i + 1}-{j + 1}"
                    print(f"Your Car id {car_id}")
                    return car_id


def leave_parking(toll_coll, car_id):
    if car_id != 0:
        toll_fee = 10
        toll_coll += toll_fee
        print("------------------")
        print(f"Car left at {car_id} , Toll Collection: {toll_fee}")
        print("------------------")
        return toll_coll
    else:
        print("------------------")
        print("NO car found to Exit from parking ! ")
        print("------------------")


def Tollamt(toll_coll):
    val = str(input("Are you Willing to donate (Y/N): ")).upper()
    if val == 'Y':
        donate_amt = 0
        print("--------------------")
        print("Your help makes a difference to save lives ")
        amt = float(input("Donation Amount: "))
        donate_amt += amt
        print(f"Your Donation amount: {donate_amt}")
        print("--------------------")
    else:
        print("--------------------")
        print(f"Your Total Collection on toll: {toll_coll}")


# Main program
slot, available, toll_coll = initial()

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
        car_id = enter_parking(slot, available)
        
        
    elif choice == 3:
        leave_parking = leave_parking(toll_coll, car_id)
        
        
    elif choice == 4:
        Tollamt(toll_coll)
        
    elif choice ==5:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")
