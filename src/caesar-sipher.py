def encrypt(secret,key):
  ascii = []
  for i in range(0,len(secret)):
    ascii.append(ord(secret[i])+key)
  encrypted = ''.join(chr(i) for i in ascii)
  return encrypted

def decrypt(secret,key):
  ascii = []
  for i in range(0,len(secret)):
    ascii.append(ord(secret[i]) - key)
  decrypted = ''.join(chr(i) for i in ascii)
  return decrypted

string_to_encode = input("Enter the message")
key = int(input("Enter the key"))

secret_en = encrypt(string_to_encode,key)
print(f"The Encrypted message is {secret_en}")
decision =  input("Do you want to decode y or n")
if(decision == 'y'):
  decrypted = decrypt(secret_en, key)
  print(decrypted)
