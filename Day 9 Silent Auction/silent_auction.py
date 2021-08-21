# Day 9 Silent Auction
# This program 
# Topics: Dictionaries, nested lists
from replit import clear
from art import logo


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


def blind_auction():
    print(logo)
    print("Welcome to the secret auction program.")

    auction_end = False
    while not auction_end:
        bid_name = input("What is your name?: ")
        bid_price = int(input("What is your bid?: $"))
        bids = {bid_name: bid_price}
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if other_bidders == "yes":
            clear()
            continue
        elif other_bidders == "no":
            auction_end = True
            find_highest_bidder(bids)
        else:
            print("Invalid input.")


blind_auction()
