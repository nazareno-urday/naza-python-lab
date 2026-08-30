"""This code is for playing blackjack
    against a computer"""

import random
from art import logo


def deal_cards():
    """Deal a card randomly"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Calculate the score of a hand"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(player_score, computer_score):
    """Compare player and computer scores"""

    if player_score == computer_score:
        return "Draw!"

    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"

    elif player_score == 0:
        return "Blackjack! You win!"

    elif player_score > 21:
        return "You went over 21. You lose!"

    elif computer_score > 21:
        return "Computer went over 21. You win!"

    elif player_score > computer_score:
        return "You win!"

    else:
        return "You lose!"


decision = input("Do you want to play a game of BlackJack? (y/n): ").lower()

if decision == "y":

    print(logo)

    player_cards = []
    computer_cards = []

    for i in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    in_game = True

    while in_game:

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print("Your cards:", player_cards, "current score:", player_score)
        print("Computer's first card:", computer_cards[0])

        if player_score == 0 or computer_score == 0 or player_score > 21:
            in_game = False

        else:
            another_card = input("Do you want to take another card? (y/n): ").lower()

            if another_card == "y":
                player_cards.append(deal_cards())

            else:
                in_game = False


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)


    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print()
    print("Your final hand:", player_cards, "final score:", player_score)
    print("Computer's final hand:", computer_cards, "final score:", computer_score)

    print(compare(player_score, computer_score))