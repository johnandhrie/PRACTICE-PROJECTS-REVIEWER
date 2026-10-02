"""
Practical Exam Practice — Rock, Paper, Scissors (Menu-Driven)
Student: [Mercado, John Andhrie M.]
"""

import random

def display_menu():
    print("\n=== Rock, Paper, Scissors Menu ===")
    print("1. Play a Round")
    print("2. View Scoreboard")
    print("3. Exit")
    return input("Choose an option: ").strip()

def play_round(scores):
    choices = ["rock", "paper", "scissors"]
    player_choice = input("\nEnter rock, paper, or scissors: ").strip().lower()
    
    if player_choice not in choices:
        print("[Error] Invalid choice. Please type rock, paper, or scissors.")
        return
        
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie! 🤝")
        scores['ties'] += 1
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round! 🎉")
        scores['player'] += 1
    else:
        print("Computer wins this round! 💻")
        scores['computer'] += 1

def view_scores(scores):
    print("\n=== Scoreboard ===")
    print(f"Your Score: {scores['player']}")
    print(f"Computer Score: {scores['computer']}")
    print(f"Ties: {scores['ties']}")

def main():
    scores = {"player": 0, "computer": 0, "ties": 0}
    running = True
    
    while running:
        choice = display_menu()
        
        if choice == '1':
            play_round(scores)
        elif choice == '2':
            view_scores(scores)
        elif choice == '3':
            print("\n=== Final Game Summary ===")
            view_scores(scores)
            print("\nExiting program. Good luck on your exam tomorrow! You've got this!")
            running = False
        else:
            print("\n[Error] Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()