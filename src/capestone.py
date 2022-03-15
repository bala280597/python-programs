import random
player1 = []
computer = []
for i in range(0,2):
    player1.append(random.randint(2,12))
print(f"your two cards are {player1}")
computer.append(random.randint(2,12))
print(f"computer first move is  {computer}")

def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum

sum_of_player1=0
sum_of_computer=0
while True:
    decision = input("Type 'yes' for another card or 'n' for pass")
    if decision == "yes":
        player1.append(random.randint(1, 12))
        print(player1,"Score:",sum(player1))

    else:
        count=0
        if sum(computer) < 17:
            while sum(computer) < 17:
                if(count == 2):
                    break
                count=count+1
                computer.append(random.randint(1, 12))
                print(computer,"Score:",sum(computer))
        else:
            computer.append(random.randint(1, 12))
            print(computer, "Score:", sum(computer))
    sum_of_player1 = sum(player1)
    sum_of_computer = sum(computer)
    if(sum_of_player1 >= 21 or sum_of_computer >= 21 ):
        if sum_of_player1 > 21:
            print('Computer won')
            break
        elif sum_of_computer > 21:
            print('Player 1 won')
            break
        elif sum_of_player1 == sum_of_computer :
            print("Draw")
        else:
           continue

def compare(a,b):
    if(a>b):
        print('Player1 won')
    else:
        print("Computer won")
