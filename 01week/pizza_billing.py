# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

pizza_s = 15
pizza_m = 20
pizza_l = 25
pepperoni_s = 2
pepperoni_o = 3
cheese = 1
if size == 's' or size == 'S':
  bill = pizza_s

elif size == 'm' or size == 'M':
  bill = pizza_m
    
elif size == 'l' or 'L':
  bill = pizza_l

if add_pepperoni == 'y' or add_pepperoni == 'Y':
  if bill == pizza_s:
    bill += pepperoni_s
  elif bill == pizza_m:
    bill += pepperoni_o
  elif bill == pizza_l:
    bill += pepperoni_o
  else:
    print('wrong selection')


if extra_cheese == 'y' or extra_cheese == 'Y':
  bill += cheese
  
elif extra_cheese == 'n' or extra_cheese =='N':
  bill == bill

print (f'Your total bill is {bill}')