from random import choice

def play():
    total_games = 0
    player_wins = 0
    computer_wins = 0

    while True:
        user = input("Please select 'r' for rock, 's' for scissor, 'p' for paper, or 'q' to quit: ").lower()
        
        if user == 'q':
            print(f"Thanks for playing! You won {player_wins} out of {total_games} games.")
            break

        choices = ['r', 'p', 's']
        computer = choice(choices)

        if user not in choices:
            print("Invalid option! Please select 'r', 'p', or 's'.")
            continue

        print(f"You chose: {user}, Computer chose: {computer}")

        if user == computer:
            print(f"It's a tie! Both chose '{user}'.")
        elif (user == 'r' and computer == 's') or \
             (user == 's' and computer == 'p') or \
             (user == 'p' and computer == 'r'):
            print("Congratulations! You won!")
            player_wins += 1
        else:
            print("You lost this round.")
            computer_wins += 1

        total_games += 1

# Run the game
play()

