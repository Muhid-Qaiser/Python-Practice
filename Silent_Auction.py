# from replit import clear
import os
from Silent_Auction_art import logo

checker = True
choice = ""
max_bid = 0
max_bidder_name = ""

print(logo, "\nWelcome to the Silent Auction!\n")

auctioners = {}

while checker:
    name = input("Enter Your Name : ")
    bid = int(input("Enter Your Bid : $"))
    auctioners[name] = bid
    choice = input("Is there anyone else who wants to bid? [yes/no] :\n")

    if choice == 'no':
        checker = False

    # clear()
    os.system("cls")

for name in auctioners:
    if auctioners[name] > max_bid:
        max_bid = auctioners[name]
        max_bidder_name = name

print(f"{max_bidder_name} is the Highest bidder with ${max_bid}.\n")
