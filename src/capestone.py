import random
player1 = []
computer = []
def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum

for i in range(0,2):
    player1.append(random.randint(2,11))
print(f"your two cards are {player1} score:{sum(player1)}")
computer.append(random.randint(2,12))
print(f"computer first move is  {computer} score:{sum(computer)}")

def compare(a,b):
    if(a>b):
        print('Player1 won')
    else:
        print("Computer won")
sum_of_player1=0
sum_of_computer=0
while True:
    decision = input("Type 'yes' for another card or 'n' for pass")
    if decision == "yes":
        player1.append(random.randint(1, 12))
        score=sum(player1)
        print(player1,"Score:",score)
        if(score == 21 ):
            print('Player 1 won')
            break
        elif score > 21:
            print("Computer won")
            break

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
            compare(sum(player1),sum(computer))
            break
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
