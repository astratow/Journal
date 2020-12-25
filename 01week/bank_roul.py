# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
names_number = len(names) - 1
names_random = random.randint(0, names_number)
print (names_random)
print (names[names_random])
