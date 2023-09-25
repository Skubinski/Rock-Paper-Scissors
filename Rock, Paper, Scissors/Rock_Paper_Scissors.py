import random
from colorama import Fore, Back, Style
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
# Player's choice
player_choice = ""
# Result
player_wins = 0
computer_wins = 0
while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == 'r':
        player_choice = rock
    elif player_move == 'p':
        player_choice = paper
    elif player_move == 's':
        player_choice = scissors

    else:
        print(Fore.RED+ "Invalid input! Try again...")
        continue
    print(f"You chose {player_choice}.")

    # Computer's choice
    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move += rock
    elif computer_random_number == 2:
        computer_move += paper
    else:
        computer_move += scissors
    print(f"The computer chose {computer_move}.")
    # Who is the winner?
    if player_choice.lower() == "rock" and computer_move.lower() == "rock":
        print(Fore.BLUE+ "Draw!")
    elif player_choice.lower() == "rock" and computer_move.lower() == "paper":
        print(Fore.RED+ "You lose!")
        computer_wins += 1
    elif player_choice.lower() == "rock" and computer_move.lower() == "scissors":
        print(Fore.GREEN+ "You win!")
        player_wins += 1
    elif player_choice.lower() == "paper" and computer_move.lower() == "rock":
        print(Fore.GREEN+ "You win!")
        player_wins += 1
    elif player_choice.lower() == "paper" and computer_move.lower() == "paper":
        print(Fore.BLUE+ "Draw!")
    elif player_choice.lower() == "paper" and computer_move.lower() == "scissors":
        print(Fore.RED+ "You lose!")
        computer_wins += 1
    elif player_choice.lower() == "scissors" and computer_move.lower() == "rock":
        print(Fore.RED+ "You lose!")
        computer_wins += 1
    elif player_choice.lower() == "scissors" and computer_move.lower() == "paper":
        print(Fore.GREEN+ "You win!")
        player_wins += 1
    elif player_choice.lower() == "scissors" and computer_move.lower() == "scissors":
        print(Fore.BLUE+ "Draw!")
    print(Style.RESET_ALL)
    print("Result:")
    print(f"Player - {player_wins}")
    print(f"Computer - {computer_wins}")
    print()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break



