#imports
import random
import game_data
#import art

# variables declaration:

data_length = len(game_data.data) #length of the list needed to limit randomint()
game_over = False # set as false, so it plays until it's True
point_count = 0 # counts points
first_choice = -1 # this one is a bit weird, but it helps to create if statement later in order to compare first with second

while not game_over:  
    print(f"Points: {point_count} ")
  
#generates first choice and pops up second choice to first in following round
    if not first_choice >= 0:
        first_choice = random.randint(0, data_length - 1)
    elif first_choice >= 0:
        first_choice = second_choice
    else:
        print('First choice could not be generated')
#generates second choice
    second_choice = random.randint(0, data_length - 1)
    
    print("############################")
  
#ensures second choice is not the same as first
    while second_choice == first_choice:
        second_choice = random.randint(0, data_length - 1)

#prints out first_choice except follower_count
    for key in game_data.data[first_choice]:
        if key != 'follower_count':
            print(game_data.data[first_choice][key])
      
    first_choice_name = game_data.data[first_choice]["name"]
    first_choice_followers = game_data.data[first_choice]["follower_count"]
  
#prints second_choice except follower_count
    print("############################")
    for key in game_data.data[second_choice]:
        if key != 'follower_count':
            print(game_data.data[second_choice][key])
      
    print("############################")
    second_choice_name = game_data.data[second_choice]["name"]
    second_choice_followers = game_data.data[second_choice]["follower_count"]

#print(game_data.data[second_choice])
    player_choice = input(f"Is {second_choice_name} higher? Y|N: \n").lower()
  
#if statement displays turn results
    if game_data.data[second_choice]["follower_count"] > game_data.data[first_choice]["follower_count"] and player_choice == 'y':
        print(f'Right!\n {second_choice_name} has {second_choice_followers} followers\n{first_choice_name} has only {first_choice_followers} followers')
    elif game_data.data[second_choice]["follower_count"] < game_data.data[first_choice]["follower_count"] and player_choice == 'n':
        print(f'Right!\n{second_choice_name} has {second_choice_followers} followers\n{first_choice_name} has {first_choice_followers} followers')
    else:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(f'$ Wrong!\n$ {second_choice_name} has {second_choice_followers} followers \n$ {first_choice_name} has {first_choice_followers} followers\n$ You earned {point_count} point[s].\n$ Game over!')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        game_over = True
    point_count = point_count + 1
  