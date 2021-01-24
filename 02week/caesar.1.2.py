alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


should_end = False
while not should_end:
  direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
  if direction == 'e':
    direction = 'encode'
  elif direction == 'd':
    direction = 'decode'
  else:
    #closes app if wrong key pressed
    print(f'{direction} is not valid option. Please try again.')
    quit()
    

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Type any key to continue. If you want to exit type 'e' and press ENTER.\n")
  if result == 'e':
    should_end = True
    print('Thank you for using Caesar Cipher! Goodbye!')
