# Day 11 Blackjack Capstone Project
# Assumptions:
#   The deck is unlimited in size.
#   There are no jokers.
#   The Jack/Queen/King all count as 10.
#   The the Ace can count as 11 or 1.
#   The cards in the list have equal probability of being drawn.
#   Cards are not removed from the deck as they are drawn.

from art import logo
import random


def deal_cards(hand):
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return hand.append(random.choice(cards))


def calculate_score(hand):
    total = sum(hand)
    if len(hand) == 2 and total == 21:
        return 0

    if 11 in hand:
        if total > 21:
            hand.remove(11)
            hand.append(1)
            total = calculate_score(hand)

    return total


start_game = True
while start_game:
    play_game = input("Would you like to play a game of Blackjack? Type 'yes' to play or 'no' to quit.\n")
    if play_game == "yes":
        break
    elif play_game == "no":
        print("Farewell!")
        start_game = False
        exit()
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        continue

print(logo)

player_hand = []
dealer_hand = []
deal_cards(player_hand)
deal_cards(player_hand)
deal_cards(dealer_hand)
deal_cards(dealer_hand)
print(player_hand)
print(dealer_hand)

card_sum = calculate_score(player_hand)
card_sum2 = calculate_score(dealer_hand)
print(f"Player total: {card_sum}")

