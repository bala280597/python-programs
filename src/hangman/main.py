import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
hangman_len = len(stages) - 1
str = random.choice(word_list)
str_len = len(str)
lists=[]
output=[]
print("Welcome to Hangman game")
print(logo)
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
      print(stages[hangman_len])
      hangman_len -= 1

    if(game==length):
        print("Game win")
    if(count==6):
      print("Game over")
      print(f"The word is {str}")
      break;
