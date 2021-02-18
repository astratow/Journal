import random
import game_data
import logo
data_length = len(game_data.data)



game_over = False


  

first_choice = -1
while not game_over:
  
  if not first_choice >= 0:
    first_choice = random.randint(0, data_length - 1)
  elif first_choice >= 0:
    first_choice = second_choice
  else:
    print('First choice could not be generated')

  second_choice = random.randint(0, data_length - 1)
  while not second_choice == first_choice:
    second_choice = random.randint(0, data_length - 1)
  print(first_choice)
  print(second_choice)
  print("######################################")
  while second_choice == first_choice:
    second_choice = random.randint(0, data_length - 1)

  for key in game_data.data[first_choice]:
    print(game_data.data[first_choice][key])
  print("######################################")
  for key in game_data.data[second_choice]:
    print(game_data.data[second_choice][key])
  second_choice_name = game_data.data[second_choice]["name"]
  #print(game_data.data[second_choice])
  player_choice = input(f"Is {second_choice_name} higher? Y|N: \n").lower()
  if game_data.data[second_choice]["follower_count"] > game_data.data[first_choice]["follower_count"] and player_choice == 'y':
    print('Right!')
  elif game_data.data[second_choice]["follower_count"] < game_data.data[first_choice]["follower_count"] and player_choice == 'n':
    print('Right!')
  else:
    print(' Wrong!\n Game over!')
    game_over = True
  