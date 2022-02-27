# ******************************************Project - Bid and Aution *************************************** 

from replit import clear
from art import logo
 
print(logo)
Auction_Required = True
Auction_Bids = []

name = input("Enther Your Name:")
amount = int(input("Enther your Bid $:"))

# Function to take multiple entries from the user
def add_bid(name, amount):
  new_bid = {
    "name": name,
    "amount": amount
  }
  Auction_Bids.append(new_bid)

add_bid(name, amount)

# Function to calculate the highest bid and their name
def calculate_bid_winner(Auction_Bids):
  winner_score = max(Auction_Bids, key=lambda x:x['amount'])
  print(f"Winner for the Autions is {winner_score['name']} with Bid amount ${winner_score['amount']}")

# Following code allows user to bid multiple users
while Auction_Required:
  bid_required = input("Are there any other bidders? (yes/no)").lower()
  clear()
  if bid_required == "yes":
    name_1 = input("Enther Your Name:")
    amount_1 = int(input("Enther your Bid $:"))
    add_bid(name=name_1, amount=amount_1)
    Auction_Required = True
  elif bid_required == "no":
    calculate_bid_winner(Auction_Bids)
    Auction_Required = False
  else:
    print("Enter Valid Option")
  


