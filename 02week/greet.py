def greet():
  name = input('Hello, what is your name?\n')
  print(f'Welcome {name}!')
  print('How are you?')
#greet()
def greet_with(name, location):
  name = input('Please enter your name:\n')
  location = input('Please tell us where are you:\n')
  print(f'You are {name} from {location}')
greet_with('name', 'location')