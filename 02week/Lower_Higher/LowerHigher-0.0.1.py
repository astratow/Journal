import random
import game_data
import logo
data_length = len(game_data.data)

first_choice = random.randint(0, data_length - 1)

print(first_choice)

second_choice = random.randint(0, data_length - 1)

print(second_choice)

while second_choice == first_choice:
  second_choice = random.randint(0, data_length - 1)
print(game_data.data[first_choice])
print(game_data.data[second_choice])