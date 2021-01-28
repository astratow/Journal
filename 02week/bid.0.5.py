from replit import clear
from art import logo
print(logo)
def bid_win(bid_log):
  bid_win = 0
  bidder_win = ""
  for bidder in bid_log:
    bid_amount = bid_log[bidder]
    if bid_amount > bid_win:
      bid_win = bid_amount
      bidder_win = bidder
  print(f"The winner is {bidder_win} with the bid of ${bid_win}.")

bid_data = {}
bid_exit = False
while not bid_exit:
  bidder_name = input("What is your name?\n")
  bidder_price = int(input("Please type your bid:\n$"))
  bid_data[bidder_name] =  bidder_price 
  bid_next = input("Do you want to continue bidding? Press 'y' to continue or type 'n' to close the auction.\n")
  if bid_next == 'n':
    bid_exit = True
    bid_win(bid_data)
  else:
    clear()
