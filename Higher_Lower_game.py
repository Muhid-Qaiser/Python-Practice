from Higher_Lower_game_data import data
import os
from Higher_Lower_game_art import logo, vs
import random
# import replit


def compare(person1, person2):
    if data[person1]["follower_count"] > data[person2]["follower_count"]:
        return 'A'
    elif data[person1]["follower_count"] < data[person2]["follower_count"]:
        return 'B'
    else:
        return 'Tie'


def winner(person1, person2):
    if data[person1]["follower_count"] > data[person2]["follower_count"]:
        return person1
    else:
        return person2


person1 = random.randint(0, len(data)-1)
person2 = random.randint(0, len(data)-1)
score = 0
game_over = False

while person2 == person1:
    person2 = random.randint(0, len(data))

print(logo)

while not game_over:

    # print(data[person1], vs , data[person2])
    print(
        f"Compare A: {data[person1]['name']}, {data[person1]['description']}, {data[person1]['country']}")

    print(vs)

    print(
        f"Against B: {data[person2]['name']}, {data[person2]['description']}, {data[person2]['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    result = compare(person1, person2)

    # replit.clear()
    os.system("cls")

    print(logo)

    if choice == result or result == "Tie":
        score += 1
        print(f"Correct guess. Current score : {score}.")
        person1 = person2
        person2 = random.randint(0, len(data))

        while person2 == person1:
            person2 = random.randint(0, len(data))
    else:
        print(f"Incorrect guess. Final score : {score}.")
        game_over = True
