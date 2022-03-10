alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
  
  secret = []
  text=list(text)
  for i in range(0,len(text)):
    for j in range(0,len(alphabet)):
      if(text[i]==alphabet[j]):
        j+=shift
        if(j > len(alphabet)):
          j-=len(alphabet)
        secret.append(alphabet[j])
        break
  secret= ''.join(map(str,secret))
  return secret

def decrypt(text,shift):
  
  secret = []
  text=list(text)
  for i in range(0,len(text)):
    for j in range(0,len(alphabet)):
      if(text[i]==alphabet[j]):
        j-=shift
        if(j < 0):
          j+=len(alphabet)
        secret.append(alphabet[j])
        break
  secret= ''.join(map(str,secret))
  return secret


repeat="yes"
while repeat == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if(direction == "encode"):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher_encode=encrypt(text,shift)
    print(f"The encrypted text is {cipher_encode}")
  else:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher_decode = decrypt(text,shift)
    print(f"The encrypted text is {cipher_decode}")
  repeat = input("Do you want to continue : yes or no")
