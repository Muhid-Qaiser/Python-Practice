import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

msg = "Try Again!\n"

computer_choice = random.randint(0, 2)

moves = [rock, paper, scissors]

player_choice = int(
    input("What do you choice, Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if player_choice > 2 or player_choice < 0:
    print("Invalid Choice!\n")

else:

    if player_choice == 1:
        if computer_choice == 0:
            msg = "You Won"
        elif computer_choice == 1:
            msg = "Tie"
        else:
            msg = "You Lose"

    elif player_choice == 2:
        if computer_choice == 0:
            msg = "You Lose"
        elif computer_choice == 1:
            msg = "You Won"
        else:
            msg = "Tie"
    else:
        if computer_choice == 0:
            msg = "Tie"
        elif computer_choice == 1:
            msg = "You Won"
        else:
            msg = "You Lose"

    print(
        f"You Chose \n{moves[player_choice]} \nComputer Chose \n{moves[computer_choice]}\n{msg}")
