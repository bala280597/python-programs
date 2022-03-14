import os
print("Welcome to silent auction program")
condition = "yes"
auction_list = []
while condition == "yes":
    name = input('what is your name?')
    bid = int(input('whats your bid '))
    data = {
        'name': name,
        'bid': bid
    }
    auction_list.append(data)
    condition = input("Are there any other bidder?")
    if(condition == "yes"):
        os.system('cls')
min = 0
name = ""
for i in auction_list:
    if i["bid"] > min:
        name = i["name"]
        min = i["bid"]
print(f"The winner is {name}")
