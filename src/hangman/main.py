import random
strings= ["bee keeper","Work Man","India","Cricket","Tony Stark","Super Saint"]
str = random.choice(strings)
str_len = len(str)
lists=[]
output=[]
for i in range(0,str_len):
    if(str[i]== " "):
        continue
    lists.append(str[i])
length = len(lists)
for i in range(0,length):
    output.append("_")
condition=True
count=0
game=0
while condition==True:
    a=input("guess a letter")
    check_variable=False
    for i in range (0,length):
      if(a == lists[i]):
          output[i]=lists[i]
          lists[i]='0'
          check_variable=True
          game+=1
          print(output)
          break;
      else:
          continue
    if(check_variable==False):
      count+=1
      print(count)
    if(game==length):
        print("Game win")
    if(count==6):
      print("Game over")
      print(f"The word is {lists}")
      break;
