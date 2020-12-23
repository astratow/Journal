print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Type character in brackets to make choice") 
step1 = input("You are on the crossroad. Are you going (r)ight or (l)eft\n")
if step1 == 'r' or step1 == 'R':
  print("Great big monster has you for dinner. Game over!\n")
elif step1 == 'l' or step1 == 'L':
  print("Yo, good choice!\n")
  step2 = input("You are on front of a river. Are you (w)aiting for a boat or (s)wim across?\n")
  if step2 == 'w':
    step3 = input("There is 3 houses: one with (b)lue door, another with (r)ed door and third with (g)reen door. Where do you go?\n")
    if step3 == 'r' or step3 == 'R':
      print("Red door are trapped! Game over!")
    elif step3 == 'b' or step3 == 'B':
      print("You found a treasure! You are a winner!")
    elif step3 == 'g'or step3 == 'G':
      print("You are teleported to different world. Game over!")
    else:
      print("You hit wrong key! Game over!")    
  elif step2 == 's' or step2 == 'S':
    print("Current drowns you. Game over!")
  else:
    print("You typed wrong character. Game over!")
else:
  print("You typed wrong letter. Game over!")
  
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload