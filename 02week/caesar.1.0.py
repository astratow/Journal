alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(ceasar_text, shift_amount, shift_direction):
  if direction == 'e':
    cipher_text = ""
    for letter in ceasar_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
  elif direction == 'd':
    plain_text = ""
    for letter in ceasar_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

caesar(ceasar_text = text, shift_amount = shift, shift_direction = direction)