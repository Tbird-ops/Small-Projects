alphabet = 'abcdefghijklmnopqrstuvwxyz '

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, key):
  encrypted = ''

  # split the message to the lenth of the key
  split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))] # Start, end, step

  # want to convert the message to index and add the key (Mod 26)
  for each_split in split_message:
    i = 0
    for letter in each_split:
      number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
      encrypted += index_to_letter[number]
      i += 1

  return encrypted


def decrypt(cipher, key):
  decrypted = ''

  # split the cipher to the length of the key
  split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))] # Start, end, step

  # convert cipher to index and subtract key (Mod 26)
  for each_split in split_cipher:
    i = 0
    for letter in each_split:
      number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
      decrypted += index_to_letter[number]
      i += 1

  return decrypted

def main():
  print("Welcome to the automated Vigenere cipher.\n")
  repeat = True
  while repeat == True:
    choice = input('Encrypt or Decrypt? (e/d)\n')
    if choice[0] == "e":
      key = input('\n\nWhat is your secret key?\n')
      message = input('\n\nWhat is your message?\n')
      encrypted_message = encrypt(message, key)
      print('Original message: ' + message)
      print('Encrypted message: ' + encrypted_message)
      input("press enter to quit")
    elif choice[0] == "d":
      key = input('\n\nWhat is your secret key?\n')
      encrypted_message = input('\n\nWhat is your encrypted message?\n')
      decrypted_message = decrypt(encrypted_message, key)
      print('\nDecrypted message: ' + decrypted_message)
      input("\npress enter to quit\n")
    else:
      print("\nSorry. Input not registered\n")

main()
