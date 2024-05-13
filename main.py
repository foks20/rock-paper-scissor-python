import random

choices = ["rock", "paper", "scissor"]

computer_choice = random.choice(choices)
my_choice = None

while my_choice not in choices:
    my_choice = input("rock paper or scissor").lower()
    
    if my_choice ==computer_choice:
        print("it's a tie")
    elif my_choice == "rock":
        if(computer_choice =="paper"):
            print("computer wins")
        else:
            print("player wins")
    elif my_choice == "paper":
        if(computer_choice =="scissor"):
            print("computer wins")
        else:
            print("player wins")
    else:
        if(computer_choice =="rock"):
            print("computer wins")
        else:
            print("player wins")
