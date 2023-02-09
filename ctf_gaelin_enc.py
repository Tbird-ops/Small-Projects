# Ultra secure encryptor

# encoded_string = 0
# msg_letters = [ord(letter) for letter in input("Message to encrypt:")]
# print(msg_letters)
# offsets = [ord(key_char) for key_char in input("Secret key:")]
# print(offsets)

# apple = 0
# for value in offsets:
#     apple += value
#     apple %= 256

# for grape in range(len(msg_letters)):
#     msg_letters[grape] ^= grape
#     msg_letters[grape] ^= apple

# encoded_string = 0
# banana = 0
# for value in msg_letters[::-1]:
#     encoded_string += value * ((256) ** banana)
#     banana += 1
# print(encoded_string)
# print(hex(encoded_string))

flag = 0xa0b6b3bcaef2b4a6be92bcffa4a595b2bba0a488e0a6bcae
flag = int(flag)
n = 2
string = 'a0b6b3bcaef2b4a6be92bcffa4a595b2bba0a488e0a6bcae'
pairs = [string[x:x+n] for x in range(0, len(str(string)), n)]
pairs = list(map(lambda pair: int(pair, 16), pairs))
for i in range(len(pairs)):
    flag -=

print(pairs)


print(string)