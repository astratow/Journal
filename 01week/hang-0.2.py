#hang-0.2.1.py
#while loop added so you can guess the word
import random

word_list = ["aardvark", "baboon", "camel"]
word_chosen = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is \n{word_chosen}.')

word_length = len(word_chosen)
word_matrix = ['_'] * word_length
end_of_game = False

while not end_of_game:
  print(word_matrix)
  guess = input("Guess a letter:\n").lower()
  for position in range(word_length):
      letter = word_chosen[position]
      if letter == guess:
          word_matrix[position] = letter
  print(word_matrix)
  if '_' not in word_matrix:
    end_of_game = True
    print('You win!')