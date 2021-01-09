#hang-0.2.py
#while loop added so you can guess the word
#hang-0.2.1.py
#stages list added
#hang-0.2.2
#added loosing
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
word_chosen = random.choice(word_list)
word_length = len(word_chosen)
word_matrix = ['_'] * word_length
end_of_game = False
lives = 6

while not end_of_game:
  guess = input("Guess a letter:\n").lower()
  for position in range(word_length):
      letter = word_chosen[position]
      if letter == guess:
          word_matrix[position] = letter
  if guess not in word_chosen:
    print('Wrong guess!')
    lives -= 1
    if lives == 0:
        end_of_game = True
        print('You lost!')
  print(f"{' '.join(word_matrix)}")  
  if '_' not in word_matrix:
    end_of_game = True
    print('You win!')
  print(stages[lives])
