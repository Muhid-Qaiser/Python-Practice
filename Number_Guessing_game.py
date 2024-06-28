import random
from Number_Guessing_game_art import logo


def compare(user_guess, computer_guess):
    if user_guess == computer_guess:
        return f"You guessed correct! The answer was {computer_guess}."
    elif user_guess < computer_guess:
        return "Too low."
    else:
        return "Too high."


print(logo, "\nGuess a number between 1 and 100")

total_tries = 10
tries_left = 0
game_end = False
user_guess = 0
computer_guess = 0

if input("Choose 'easy' or 'hard' mode: ") == "hard":
    total_tries = 5

computer_guess = random.randint(1, 100)

while not game_end and total_tries > tries_left:

    user_guess = int(
        input(
            f"You have {total_tries-tries_left} tries left.\nEnter your guess: "
        ))

    result = compare(user_guess, computer_guess)

    print(result)

    if result == f"You guessed correct! The answer was {computer_guess}.":
        game_end = True
    else:
        tries_left += 1

if tries_left == total_tries:
    print(
        f"You ran out of guesses. You Lost.\nThe computer's guess was {computer_guess}.")
