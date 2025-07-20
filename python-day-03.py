# checking the number for even or odd
num = int(input("Enter the number : "))

n = num % 2

if n == 1 :
    print("This is an odd number!")
else :
    print("This is even number!!")







# bmi calculator
height = float(input("Enter your height : "))
weight = int(input("Enter your weight : "))

bmi = round((weight/(height**2)),1)

if bmi < 18.5 :
    print("You are under weight!")
elif bmi >= 18.5 and bmi < 25 :
    print(f"your BMI is : {bmi}\nYou are normal weight.")
elif bmi >= 25 and bmi < 30 :
    print(f"your BMI is : {bmi}\nYou are slightly over weight!!")
elif bmi >= 30 and bmi < 35 :
    print(f"your BMI is : {bmi}\nYour are slightly obese!!!")
else :
    print(f"your BMI is : {bmi}\nYou are clinically obese!!!!..")





# leap year calculator
year = int(input("Enter the year : "))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("This is leap-year.")
        else :
            print("This is not a leap-year.")
    else :
        print("This is a leap-year.")
else :
    print("This is not a leap-year.")






# pizza order
print("Welcome to python pizza delivery!")
size = input("What size pizza do you want? S , M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S" :
    bill = 15
    if add_pepperoni == "Y" :
        extra_amount = 2
    else :
        extra_amount = 0

elif size == "M" :
    bill = 20
    if add_pepperoni == "Y" :
        extra_amount = 3
    else :
        extra_amount = 0

else :
    bill = 25
    if add_pepperoni == "Y" :
        extra_amount = 3
    else :
        extra_amount = 0

total_bill = bill + extra_amount

if extra_cheese == "Y" :
    total_bill += 1
else :
    total_bill += 0

print(f"Your final bill is : ${total_bill}")






# love calculator

print("welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


calculate_name = name1.lower() + name2.lower()

n1 = calculate_name.count("t")
n2 = calculate_name.count("r")
n3 = calculate_name.count("u")
n4 = calculate_name.count("e")

m1 = calculate_name.count("l")
m2 = calculate_name.count("o")
m3 = calculate_name.count("v")
m4 = calculate_name.count("e")

first_digit = str(n1 + n2 + n3 + n4)
second_digit = str(m1 + m2 + m3 + m4)

score = int(first_digit + second_digit)

if score < 10 or score > 90 :
    print(f"Your score is {score} , You go together like coke and mentos. ")
elif score >= 40 and score <=50 :
    print(f"Your score is {score} , you are alright together. ")
else :
    print(f"Your score is {score}.")






# treasure island game
print('''
       
         ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___   
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~ 
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~         
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-        
             ~\_        // *******.:|\^^^/|:.******* \\        _/~             
                \      / ********.::(>: :<)::.******** \      /                
                 \   /  ********.::::\\|//::::.********  \   /                 
                  \ /   *******.:::::(o o):::::.*******   \ /                  
                   /.   ******.::::'*|V_V|***`::.******   .\                   
                     ~~--****.:::'***|___|*****`:.****--~~                     
                           *.::'***//|___|\\*****`.*                           
                           .:'  **/##|___|##\**    .                           
                          .    (v(VVV)___(VVV)v)
                          
                          
                          
                    ====-_  _-====___                              
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
       
''')

print("Welciome to the treasure island.\nYour mission is to find the treasure.")

path = input('You are at a cross road. where do you want to go? Type "left" or "right" \n').lower()

if path == "left" :
    lake = input('You come to lake. there is an island middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if lake == "wait" :
        door = input("You arrived at the island unharmed. There is a house with three doors. one red ,one blue and one yellow. Which color do you choose? \n").lower()
        if door == "yellow" :
            print("Congratulation. You won...")
        elif door == "red" :
            print("You entered a wild beast room. Game over!!!")
        else :
            print("You entered a door that not exist. Game over!!!")
    else :
        print("You can't swim so much time to reach the island. Game over!!!")


else :
    print("You felt into a hole. Game over!!!")









