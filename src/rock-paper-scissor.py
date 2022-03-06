import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(choice)
if(choice == 0):
  print(rock)
elif(choice == 1):
  print(paper)
else:
  print(scissors)
opponent = random.randint(0,2)
if(opponent == 0):
  print(rock)
elif(opponent == 1):
  print(paper)
else:
  print(scissors)
if((choice == 0 and opponent == 2) or (choice == 1 and opponent == 2) or (choice == 2 and opponent == 0)):
  print("Winner")
else:
  print("Lost")
