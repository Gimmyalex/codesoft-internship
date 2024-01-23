import random

def determine_winner(user_choice, computer_choice):
    # Game logic to determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        # Prompt the user to choose rock, paper, or scissors
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate a random choice for the computer
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Determine the winner and display the result
        result = determine_winner(user_choice, computer_choice)
        print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
        print(result)

        # Update scores
        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        # Display scores
        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        # Ask the user if they want to play another round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
