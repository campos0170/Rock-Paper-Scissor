from random import choice


def play():

    total_games = 0
    player_wins = 0
    computer_wins = 0
  
    while True:

        user = input("Please select 'r' for rock, 's' for scissor and, 'p' for paper, q for quit if you no longer want to play: ")
        
        if user == 'q'.lower():
            print(f"Thanks for playing! You won a total of '{player_wins}' out of {total_games} games.")

            break

        choices = ['r','p','r']

        computer = choice(choices)

        # The following if ststement determines if we have a tie in the game, meaning both the computer and
        # user made the same choice.

        if user not in choices:
            print("Please enter a valid option")

        elif user == computer:
            print( f"You and the computer both selected '{user}', we have a Tie!")
            total_games+=1

        elif (user == 'r' and computer == 'p') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            print("Congratulations! You won!")
            player_wins +=1
            total_games+=1
        
        else:
            
            print( "You lost")
            computer_wins+=1
            total_games+=1
play()

