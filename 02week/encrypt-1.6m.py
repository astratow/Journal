alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '(e)ncode' to encrypt, type '(d)ecode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text_plain, shift_length):
  alphabet_position_new = 0
  text_list = list(text)
  for letter in text_list:
    #print(i)
    alphabet_position = alphabet.index(letter)
    alphabet_position += shift_length
    #print(alphabet_position)
    if alphabet_position > 25:
      alphabet_position -=  26
    
    text_list[alphabet_position_new] = alphabet[alphabet_position]
    alphabet_position_new += 1
  text_encrypted = ''.join(text_list)
  print(f'Encoded text is {text_encrypted}')
def decrypt(text_cipher, shift):
  alphabet_position_new = 0
  text_list = list(text)
  for letter in text_cipher:
    alphabet_position = alphabet.index(letter)
    alphabet_position -= shift

    if alphabet_position < 0:
      alphabet_position += 26
    text_list[alphabet_position_new] = alphabet[alphabet_position]
    alphabet_position_new += 1 
  text_decrypted = ''.join(text_list)
  print(f'Decoded text is {text_decrypted}')
if direction == 'e' or direction == 'encode':
  encrypt(text_plain = text, shift_length = shift)
elif direction == 'd' or direction == 'decode':
  decrypt(text_cipher = text, shift = shift)
else:
  print('Error. Wrong selection, please try again.')