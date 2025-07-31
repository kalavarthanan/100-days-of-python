fruits = ['apple','orange','pineapple']

for i in fruits :
    print(i)




# find the average the set of data as input
student_heights = input("Input a list of heights : ").split()

print(student_heights)
print(student_heights[0])
print(type(int(student_heights[0])))

count = 0

for i in student_heights :
    count = count + 1

print(count)
total_height = 0

for i in range(0,count) :
    student_heights[i] = int(student_heights[i])
    total_height += student_heights[i]

average = int(round(total_height / count))

print(f"Average height of the students is : {average}")






# student_heights = input("Input a list of heights : ").split()

count = 0
totalheight = 0
for height in student_heights :
    count += 1
    studentheight = int(height)
    totalheight = totalheight + studentheight


print(round(totalheight / count))













# calculate the highest value in tha list using for loop

students_score = input("Input a list of student's marks :").split()

count = 0
for i in students_score :
    count += 1


max = 0
for i in range(0,count) :
    students_score[i] = int(students_score[i])
    if (students_score[i] > max) :
        max = students_score[i]
    else :
        max = max


print(f"The highest score in the class is : {max}")





# calculate the highest value in tha list using for loop
students_score = input("Input a list of student's marks :").split()

for i in range(0,len(students_score)) :
    students_score[i] = int(students_score[i])


highest_score = 0
for score in students_score :
     if score > highest_score :
         highest_score = score

print(f"The highest score in the list is : {highest_score}")





total = 0
for i in range(2,101,2) :
    total += i
print(total)



for i in range(1,101) :
    if (i % 3 == 0 and i % 5 == 0) :
        print("FizzBuzz")
    elif (i % 5 == 0) :
        print("Buzz")
    elif (i % 3 == 0) :
        print("Fizz")
    else :
        print(i)

