# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name3 = (name1 + name2)
name3 = name3.lower()
print(name3)

t = name3.count('t')
r = name3.count('r')
u = name3.count('u')
e = name3.count('e')
nameT = t + r + u + e
l = name3.count('l')
o = name3.count('o')
v = name3.count('v')
e = name3.count('e')
nameL = l + o + v + e
print(nameT)
if nameT < 1 or nameT >= 9:
  print(f"Your score is **{nameT}{nameL}**, you go together like coke and mentos.")
elif nameT >=4 and nameT <=5:
  print(f"Your score is **{nameT}{nameL}**, you are alright together.")
else:
  print(f'Your score is {nameT}{nameL}')
