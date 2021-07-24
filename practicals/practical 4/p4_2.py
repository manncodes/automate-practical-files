# make rock paper sicissors game

import random

print("\nWelcome to the rock paper scissors game")
print("\nThe rules are simple, you will be asked to enter rock, paper or scissors")
print("\nThen the computer will randomly choose rock, paper or scissors")
print("\nThen the winner will be decided")
print("\nGood luck")

while True:
    print("\nPlease enter rock, paper or scissors")
    player = input("\nEnter your choice: ")
    player = player.lower()
    if player == "rock":
        print("\nPlayer chose rock")
    elif player == "paper":
        print("\nPlayer chose paper")
    elif player == "scissors":
        print("\nPlayer chose scissors")
    else:
        print("\nPlease enter rock, paper or scissors")
        continue

    comp = random.randint(1, 3)
    if comp == 1:
        print("\nComputer chose rock")
    elif comp == 2:
        print("\nComputer chose paper")
    elif comp == 3:
        print("\nComputer chose scissors")
    else:
        print("\nComputer chose a random number")

    if comp == 1:
        if player == "rock":
            print("\nIt's a tie")
        elif player == "paper":
            print("\nComputer wins")
        elif player == "scissors":
            print("\nPlayer wins")
    elif comp == 2:
        if player == "rock":
            print("\nPlayer wins")
        elif player == "paper":
            print("\nIt's a tie")
        elif player == "scissors":
            print("\nComputer wins")
    elif comp == 3:
        if player == "rock":
            print("\nComputer wins")
        elif player == "paper":
            print("\nPlayer wins")
        elif player == "scissors":
            print("\nIt's a tie")
    else:
        print("\nPlease enter rock, paper or scissors")

    print("\nWould you like to play again? (y/n)")
    answer = input("\nEnter your choice: ")
    answer = answer.lower()
    if answer == "n":
        break
    else:
        continue
print("\nGoodbye")
