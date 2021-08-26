# Task 4

# Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.

# Remember the rules:
#
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock
#.......................................................................................................................
from typing import Dict

def winner(player_1: str, player_2: str) -> [str]:

    game_dictionary: Dict = {'1':'3', '3':'2', '2':'1', 'rock':'scissors', 'scissors':'paper', 'paper':'rock'}

    if game_dictionary[player_1] == player_2 :
        return "\n Player 1 Won! Congratulations !!"

    elif game_dictionary[player_2] == player_1 :
        return " \n Player 2 Won! Congratulations !!"

    else:
        return "It's a Draw !"


#---------------------------------------------------------------------------------------------------------------------

def input_from_players() -> [str]:

    print("\n***** Welcome to Rock-Paper-Scissors Game *****","\nChoose the Number or type\t1. Rock\t2. Paper\t3. Scissors")
    player_1: str = input("\nPlayer_1 : choose the number  1. Rock 2. Paper 3. Scissors :")
    player_2: str = input("Player_2 : choose 1.Rock 2.Paper 3.Scissors :")

    return winner(player_1, player_2)
#----------------------------------------------------------------------------------------------------------------------

print(input_from_players())
# condition to ask for playing again

while True :
    play_again: str = input("\nDo you want to play Again..?  y/n")

    if play_again == "y" :
        print(input_from_players())

    else:
        exit()
