from ascii import logo
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def select_the_winner(auction):
    winner = ""
    winers_bid = 0
    no_same_bids = True
    for bidder in auction:
            if auction[bidder] > winers_bid:
                winers_bid = auction[bidder]
                winner = bidder
            elif auction[bidder] == winers_bid:
                no_same_bids = False
    if no_same_bids:
        print(f"The winner is {winner} with a bid of ${winers_bid}")
    else:
        print("We have several users with the same bids. Please try again.")

print(logo)

app_runing = True
auction = {}

while app_runing:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    more_users = input("Are there any other bidders? Type 'yes' or 'no': ")
    if more_users == "no":
        app_runing = False
        clear()
        select_the_winner(auction)
    elif more_users == "yes":
        clear()
    else:
        app_runing = False
        print("Please start again and follow the instructions.")
