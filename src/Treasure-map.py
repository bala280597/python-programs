row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position=int(position)
ten= int((position/10)-1)
digit = int((position % 10)-1)
map[digit][ten] = 'X'
print(f"{row1}\n{row2}\n{row3}")
