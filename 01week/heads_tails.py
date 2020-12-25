import random
result = random.randint(0, 1)
print ('Welcome to famous game Heads or Tails! In this game you choose one of two options:\n Heads or Tails,\nthen we throw coin in the air and if your guess was right, you win.\n') 
selector = input('Please choose one of two option: (H)eads or (T)ails?\n').lower()
if selector == 'h' and result == 1:
  print ('Congratulations! You won!')
elif selector == 't' and result == 0:
  print ('Congratulations! You won!')
elif selector == 'h' and result == 0:
  print ('I am very sorry but you lost!')
elif selector == 't' and result == 1:
  print ('I am very sorry but you lost!')
else:
  print ('You hit wrong character. Please try again. Game over!')