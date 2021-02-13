############### Blackjack Project #####################
import random


print('############### Blackjack Project #####################')
def deal_card():
  """Returns random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card_dealt = random.choice(cards)
  return card_dealt

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  print(f"cards are {cards}")
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    print(cards)
    cards.append(1)
    print(cards)
  return sum(cards)

def compare(score_user, score_computer):

  if score_user > 21 and score_computer > 21:
    return "You went over. You lose 😤"
  if score_user == score_computer:
    return "Draw 🙃"
  elif score_computer == 0:
    return "Lose, opponent has Blackjack 😱"
  elif score_user == 0:
    return "Win with a Blackjack 😎"
  elif score_user > 21:
    return "You went over. You lose 😭"
  elif score_computer > 21:
    return "Opponent went over. You win 😁"
  elif score_user > score_computer:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  cards_user = []
  cards_computer = []
  game_over = False

  for _ in range(2): 
    cards_user.append(deal_card())   
    cards_computer.append(deal_card())
   
  

  while not game_over:
    
    score_user = calculate_score(cards_user)
    score_computer = calculate_score(cards_computer)
    print(f"   Your cards: {cards_user}, current score: {score_user}")
    print(f"   Computer's first card: {cards_computer[0]}")
    if score_computer == 0 or score_user == 0 or score_user > 21:
      game_over = True
    else:
      more = (input("Would you like to draw another card?\n 'Y'/'N'\n")).lower()
      
      if more == 'y':
        cards_user.append(deal_card())
        #print(cards_user)
      else:
        game_over = True 

  while score_computer != 0 and score_computer > 17:
    cards_computer.append(deal_card())
    score_computer = calculate_score(cards_computer)
  print(f"   Your final score is: {score_user}")
  print(f"   Computer final score is: {score_computer}")
  print(compare(score_user, score_computer))

while input('Would you like to play Blackjack?\n Type Y/N please:\n').lower() == 'y':
  
  play_game()
