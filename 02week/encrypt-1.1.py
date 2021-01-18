
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt():
  j = 0
  textList = list(text)
  for i in textList:
    #print(i)
    alphabetPosition = alphabet.index(i)
    alphabetPosition += shift
    #print(alphabetPosition)
        if alphabetPosition > 25:
            alphabetPosition = alphabetPosition - 26
    
    textList[j] = alphabet[alphabetPosition]
    j += 1
  textEncrypted = ''.join(textList)
  print(f'Encoded text is {textEncrypted}')

    
encrypt()