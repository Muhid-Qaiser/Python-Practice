import random


def get_choice():
    player_choice = input("\nEnter choice (Rock,Paper,Scissors) : ")

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    choices = {"Player": player_choice, "Computer": computer_choice}

    return choices


def check_win(Player, Computer):

    print(f"\nYou Chose : {Player}, Computer Chose : {Computer} \n")

    if Player == Computer:
        return "It's a Tie!"

    elif Player == "Rock":
        if Computer == "Paper":
            return "Paper Covers Rock! Computer Wins!"
        else:
            return "Rock Smashes Scissors! You Win!"

    elif Player == "Paper":
        if Computer == "Rock":
            return "Paper Covers Rock! You Win!"
        else:
            return "Scissors Cuts Paper! Computer Wins!"

    elif Player == "Scissors":
        if Computer == "Rock":
            return "Rock Smashes Scissors! Computer Wins!"
        else:
            return "Scissors Cuts paper! You Win!"


choices = get_choice()
print(check_win(choices["Player"], choices["Computer"]))

print("\n")
