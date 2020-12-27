rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcome to Rock - Paper - Scissors game!')

#user selection
selectUser = input('Please select (R)ock, (P)aper or (S)cissors by typing letter and hitting ENTER.\n').lower()
if(selectUser == 'r'):
  print(f'You choose:\n {rock}')
elif(selectUser == 'p'):
  print(f'You choose:\n {paper}')
elif(selectUser == 's'):
  print(f'You choose:\n {scissors}')
else:
  print('You typed wrong character, please try again')
  exit()

#AI selection
import random
selectAI = random.randint(1, 3)
if(selectAI == 1):
  print(f'AI selected:\n{rock}\n')
elif(selectAI == 2):
  print(f'AI selected:\n{paper}\n')
elif(selectAI == 3):
  print(f'AI selected:\n{scissors}\n')
else:
  print('Something went wrong')
  exit()

#game result
if(selectUser == 'r' and selectAI == 3):
  print('\n Rock makes Scissors dull\n Congratulations! You won!\n')
elif(selectUser == 'p' and selectAI == 1):
  print('\n Paper wraps Rock.\n Congratulations! You won!\n')
elif(selectUser == 's' and selectAI == 2):
  print('\n Scissors cut Paper.\n Congratulations! You won!\n')
elif(selectUser == 'r' and selectAI == 2):
  print('\n Paper wraps Rock.\n I am so sorry, but you lost!\n')
elif(selectUser == 's' and selectAI == 1):
  print('\n Rock makes Scissors dull.\n I am so sorry, but you lost!\n')
elif(selectUser == 'p' and selectAI == 3):
  print('\n Scissors cut Paper.\n I am so sorry, but you lost!\n')
else:
  print('\n Your selection was the same! Draw!\n')

