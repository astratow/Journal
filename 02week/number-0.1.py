#Number Guessing Game Objectives:
#from art import logo 
import random
#print(logo)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
print("Welcome to Number Guessing Game!\n")
number = random.randrange(1, 100)
print(number)
guess_correct = False
turn = 0
#guess_number = input("Enter number between 1 and 100:\n")
while not guess_correct == True:
  turn = turn + 1
  guess_number = int(input("Enter number between 1 and 100:\n"))
  if guess_number > number:
    print(f"Turn {turn}.\n {guess_number} is too high.")
  elif guess_number < number:
    print(f"Turn {turn}.\n{guess_number} is too low.")
  elif guess_number == number:
    print(f"Congratulations! {guess_number} is right!")
    guess_correct = True
  else:
    print("Unknown error")

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
