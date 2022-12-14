from replit import clear
from art import logo

# Function which is used to find the highest bidder
def find_highest_bidder(record):
  max_bid = 0
  highest_bidder = None
  for bidder in record:
    bid_amount = record[bidder]
    if bid_amount > max_bid:
      highest_bidder = bidder
      max_bid = bid_amount
  print(f"The highest bidder was {highest_bidder}, with a bid of £{max_bid}")

# Variable which will keep track of the bidders names and bids
bidding_record = {}

not_done = "yes"

# Main Loop
while not_done == "yes":
  
  print(logo)
  print("Welcome to the secret auction program! \n")
  name = input("What is your name? \n").lower() 
  bid = int(input("What is your bid in £? \n")) 
  bidding_record[name] = bid
  not_done = input("Are there any other bidders? yes or no \n").lower()
  clear()

find_highest_bidder(bidding_record)







  



