import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissor): ").capitalize()
    
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissor.")
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    return user_choice



def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])



def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def print_winner(winner, user_name):
    print(f"{user_name} {winner}")

def play_game():
    user_wins = 0
    computer_wins = 0
    user_name = input("Enter your name: ")

    for i in range(0,4):
        opp=opp+i
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n{user_name} chose {user_choice}")
        
        print(f"Computer chose {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        print_winner(winner, user_name)

        if winner == "You win!":
            user_wins += 1
        elif winner == "Computer wins!":
            computer_wins += 1

    print("\nFinal Results:")
    print(f"{user_name}: {user_wins} wins")
    print("Computer: wins".format(computer_wins))

    if user_wins > computer_wins:
        
        print("\nCongratulations! You are the overall winner!")
    elif user_wins < computer_wins:
        
        print("\nSorry, the computer is the overall winner.")
    else:
        
        print("\nIt's a tie overall.")

if __name__ == "__main__":
    play_game()
