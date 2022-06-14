from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
print(logo)
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What's your bid? "))
    bids[name] = price
    should_continued = input(
        "Are there any other bidder? type 'yes' or 'no'\n ").lower()
    if should_continued == "no":
        bidding_finished = True
    elif should_continued == "yes":
        clear()

find_highest_bidder(bids)
