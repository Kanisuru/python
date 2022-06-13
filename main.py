import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors? ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win!")
        elif computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose!")
        elif computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose!")
        elif computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")