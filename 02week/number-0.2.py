 
import random

print("Welcome to Number Guessing Game!\n")
level_selector = input("Please choose difficulty level:\nE for Easy\nN for Normal\nH for Hard\n").lower()
def difficulty_level(level):
  if level_selector == 'e':
    max_turns = 15
    print("Level EASY.\nLives: 15")
  elif level_selector == 'n':
    max_turns = 10
    print("Level NORMAL.\nLives: 10")
  elif level_selector == 'h':
    max_turns = 5
    print("Level HARD.\nLives: 5")
  else:
    print("Unknown error") 

  return max_turns

number = random.randrange(1, 100)

game_over = False
lives = difficulty_level(level_selector)

while not game_over == True:
  lives = lives - 1

  guess_number = int(input("Enter number between 1 and 100:\n"))
  if guess_number > number:
    print("\nYou have {lives} lives left.\n {guess_number} is too high.\n Have another go.")
  elif guess_number < number:
    print(f"You have {lives} lives left.\n{guess_number} is too low.\n Have another go.")
  elif guess_number == number:
    print(f"Congratulations! {guess_number} is right!")
    game_over = True
  else:
    print("Unknown error")
  if lives == 0:
    print("You run out of lives. Game over.")
    game_over = True