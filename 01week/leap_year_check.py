# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 400 == 0:
  print (f"Year {year} is a leap year")
elif year % 100 == 0:
  print (f"Year {year} is not a leap year")
elif year % 4 == 0:
  print (f"Year {year} is a leap year")
else:
  print (f"Year {year} is not a leap year")
