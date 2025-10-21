
                                       # Stone Paper Scissors Game #

import random   

choices = ["stone","paper","scissors"] # Available choices
while True:
    # Taking input from user
    you = input("\n Enter your choice(stone/paper/scissors),or 'quit' to stop:").lower()
    if you =="quit":       # if user wants to quit
        print("Game over.Thanks for playing !")
        break
    if you not in choices:          # if user enters invalid choice 
        print("Invalid choice ! Please choose Stone,Paper,Scissors.")
        continue
    computer = random.choice(choices)
    print(f"You chose {you}\n Computer chose {computer}")
    if you == computer:
        print("It's a draw !")  # If both choices are same
    elif(you == "stone" and computer == "scissors")or( you =="scissors"and computer == "paper")or(you == "paper" and computer == "stone"):
        print("You Win !")   # Winning conditions
    else:
        print("You Lose !") # Losing conditions