Strings = "bee keeper"
str_len = len(Strings)
lists=[]
for i in range(0,str_len):
    if(Strings[i]== " "):
        continue
    lists.append(Strings[i])
length = len(lists)
condition=True
count=0
game=0
while condition==True:
    a=input("guess a letter")
    check_variable=False
    for i in range (0,length):
      if(a == lists[i]):
          lists[i]='0'
          check_variable=True
          game+=1
          print(lists)
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
      break;
