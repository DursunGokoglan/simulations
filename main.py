# Suppose you're on a game show, and you're given the choice of three doors:
# Behind one door is a car; behind the others, goats.
# You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door,
# say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?"
# Is it to your advantage to switch your choice?

import random

number_of_doors = 3
switch_status = False  # Change to True to see if it matters
winning_status = False


def game():
    global number_of_doors, switch_status, winning_status

    players_door = random.randint(1, number_of_doors)
    if players_door == 1:
        winning_status = True

    if switch_status is True:
        winning_status = not winning_status

    if winning_status is True:
        return 1
    else:
        return 0


def sim(redo_count):
    global winning_status
    win_count = 0

    for i in range(redo_count):
        winning_status = False
        if game() == 1:
            win_count += 1

    print(f"winrate = {win_count/redo_count}")


sim(redo_count=1000)  # Increase to see the Law of Large Numbers
