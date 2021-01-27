from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bidder_name = input("What is your name?\n")
bidder_price = input("Please type your bid:\n$")
bidder_data = {bidder_name : bidder_price}
bidder_log = []
bidder_log.append(bidder_data)
print(bidder_log)