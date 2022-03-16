import random
number = random.randint(1,100)
user_input = input('Choose the difficulty "hard" or "easy"')
if(user_input == "easy"):
    count=10
else:
    count=5
while count > 0:
  guess=int(input("Guess a number"))
  if(guess < number):
      print("Number is  big")
  elif(guess > number):
      print("Number is  small")
  else:
      print("You guess Correct")
      break
  count=count-1
if(count==0):
    print("You run out of life: Lost\n")
    print(f"Correct number is {number}")
