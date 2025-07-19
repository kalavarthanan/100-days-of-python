print the string last character
print("Hello"[len("Hello")-1])



a = input("Enter the word: ")
length = len(a)
print(a[length-1])





a = input("Enter your Name : ")

length = len(a)
num_length = str(length)
start = a[0]
end = a[length-1]
print("Your name has " + num_length + " Number of characters\n" + "Which is start with " + start + " and end with " + end)





# print the entered two digits number's addition

num = input("Enter a two digit number : ")
new_num = str(num)
start = new_num[0]
end = new_num[1]

print(start + " + " + end + " = ",(int(new_num[0]))+int(new_num[1]))




# BMI calculator

weight = int(input("Enter your weight in kg :"))
height = float(input("Enter your height in m :"))

bmi = weight/(height**2)

print("Your BMI is : ",int(bmi))




# f-string

score = 0
height = 1.8
isWinning = True

print(f"Your score is : {score}\nYour height is : {height}\nYou are winning is : {isWinning}")




age = int(input("Enter your age :"))

balance_age = 90 - age

balance_month = balance_age * 12
balance_week = balance_month * 4
balance_day = balance_week * 7

print(f"You have {balance_day} days , {balance_week} weeks and {balance_month} months left.")







# tip calculator

print("\nwelcome to the tip calculator")

bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage of bill would you like to give? 10,12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip_amount = (tip/100) * bill

total_bill = bill + tip_amount

amount_per_people = round((total_bill/number_of_people) , 2)

print(f"Each person should pay $ {amount_per_people}")













