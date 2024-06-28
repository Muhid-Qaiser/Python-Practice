import random
import os
from BlackJack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    if len(cards) == 2 and 11 in cards and 10 in cards:
        return 0

    elif 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
        return sum(cards)

    return sum(cards)


def compare(user_score, computer_score):
    if computer_score == 0:
        return "Dealer got BlackJack. You Lose."
    elif user_score == 0:
        return "You got BlackJack. You Win."
    elif user_score > 21:
        return "You went Bust. You Lose."
    elif computer_score > 21:
        return "Dealer went Bust. You Win."
    elif user_score > computer_score:
        return "You Win."
    elif computer_score > user_score:
        return "You Lose."
    elif user_score == computer_score:
        return "It's a Tie."


def BlackJack():

    print(logo, "\nWelcome to the BlackJack Game!")

    game_over = False
    choice = ""

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        choice = ""

        print(f"\nYour cards are : {user_cards}",
              f"\nDealer's first card is : [{computer_cards[0]}]")

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour score is {user_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("\nType 'y' to draw another card, 'n' to stop: ")

        if choice == 'n':
            game_over = True
        elif choice == 'y':
            user_cards.append(deal_card())

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour cards are : {user_cards}",
          f"\nDealer's cards are : {computer_cards}")

    print(f"\nYour score is {user_score} \nDealer's score is {computer_score}")

    result = compare(user_score, computer_score)
    print(f"\n{result}")

    choice = input("\nDo you want to play again? [y/n] : ")

    if choice == 'y':
        os.system('cls')
        BlackJack()
    elif choice == 'n':
        print("\nEnd Game.\n--------------------------------------------------\n")


if input("\nDo you want to play the BlackJack game? [y/n] : ") == 'y':
    os.system('cls')
    BlackJack()
else:
    print("\nExiting...\n")
