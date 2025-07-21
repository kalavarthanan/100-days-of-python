import random

random_integer = random.randint(0,4)
print(random_integer)
random_float = random.random()  #0.00000000 - 0.999999999999

print(random_integer + random_float)





test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_num = random.randint(0,1)
0 for Tails   1 for Heads
#
if random_num == 0 :
    print("Tails")
else :
    print("Heads")




random_seed = int(input("Create a seed number: "))
random.seed(random_seed)

namesAsCSV = input("Give me everybody's names, separated by a comma: \n")
names = namesAsCSV.split(",")

names_length = len(names)  #get the number of items in the list

random_num = random.randint( 0 , (names_length - 1) )   #generate the random number

person = names[random_num]

print(f"\n{person} is going to buy the meal today! ")







random_seed = int(input("Create a seed number: "))
random.seed(random_seed)

namesAsCSV = input("Give me everybody's names, separated by a comma: \n")
names = namesAsCSV.split(",")

name = random.choice(names)
print(f"{name} is going to buy the meal today!")







row1 = ["🟥","🟥","🟥"]
row2 = ["🟥","🟥","🟥"]
row3 = ["🟥","🟥","🟥"]

map = [row1, row2, row3]

print(f"{row1}\n\n{row2}\n\n{row3}")

position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
raw = int(position[1]) - 1

print(column,raw)

if (column == 0 and raw == 0) :
    row1[0] = "⬛"
elif (column == 0 and raw == 1) :
    row2[0] = "⬛"
elif (column == 0 and raw == 2) :
    row3[0] = "⬛"
elif (column == 1 and raw == 0) :
    row1[1] = "⬛"
elif (column == 2 and raw == 0) :
    row1[2] = "⬛"

elif (column == 1 and raw == 1) :
    row2[1] = "⬛"

elif (column == 2 and raw == 1) :
    row2[2] = "⬛"

elif (column == 1 and raw == 2) :
    row3[1] = "⬛"

else :
    row3[2] = "⬛"


selected_raw = map[raw]
selected_raw[column] = "⬛"


print(f"{row1}\n\n{row2}\n\n{row3}")







# rock paper scissors game

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

random_num = random.randint(0,2)

choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors: "))

print("\n\ncomputer choose : " )
if random_num == 0 :
    print(rock)
elif random_num == 1 :
    print(paper)
else :
    print(scissors)

print("You choose : ")
if choice == 0 :
    print(rock)
elif choice == 1 :
    print(paper)
else :
    print(scissors)


if (random_num == 2 and choice == 0 ) or (random_num == 2 and choice == 1 ) or(random_num == 0 and choice == 2) :
    print("You Loose!!!")
elif (random_num == 1 and choice == 0) or (random_num == 0 and choice == 1) or (random_num == 1 and choice == 2) :
    print("You Won The Game...")
else :
    print("Game is Draw..")




