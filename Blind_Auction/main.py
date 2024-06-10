from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
not_bidding = False


def find_mx_bidder(bids):
  highest_bid = 0
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount>highest_bid:
      highest_bid = bid_amount
      winner = bidder   
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not not_bidding:
  name = input("Enter your name: ")
  price = int(input("Enter your bid: $"))
  bids[name] = price
  continue_bidding = input("Continue Bidding? Y/n: ")
  if continue_bidding =="n":
    not_bidding = True
    find_mx_bidder(bids)
  elif continue_bidding == "y":
    clear()
    