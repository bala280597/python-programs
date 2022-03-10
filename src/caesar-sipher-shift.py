alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  secret = []
  text=list(text)
  for i in range(0,len(text)):
    position= alphabet.index(text[i])
    if(direction == "encode"):
      position+=shift
      if(position > len(alphabet)):
        position-=len(alphabet)
    if(direction == "decode"):
      position-=shift
      if(position > len(alphabet)):
        position+=len(alphabet)
    secret.append(alphabet[position])
  secret= ''.join(map(str,secret))
  return secret

repeat="yes"
while repeat == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  result=caesar(text,shift,direction)
  print(f"The {direction}ed text is {result}")
  repeat = input("Do you want to continue : yes or no")
