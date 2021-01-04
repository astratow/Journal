#hang-0.1.py
#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
guessed_letter = input('Please input one letter, which might be in the misterious word\n')
chosen_word = random.choice(word_list)
#print(chosen_word)
guessed_letter = guessed_letter.lower()

for letter in chosen_word:
  if guessed_letter == letter:
    print('yes')
  else:
    print('no')