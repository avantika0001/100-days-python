#for loops, range, code blocks

# fruits =["Apple","Cherry","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+" Pie")

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
# sum=0
# n=0
# for height in student_heights:
#   sum+=height 
#   n+=1
# print(sum)
# print(n)
# average_height = round(sum / n)
# print(average_height)


# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
#     # print(highest_score)
    
# print(f"The highest score in the class is: {highest_score}")

'''Range() function'''
# for number in range(1,11,3):  #steps
#     print(number)

# total=0    
# for number in range(1,101):  #steps
#     total+=number
# print(total)

#Write your code below this row 👇
# total=0
# for number in range(1,101):
#     if(number%2==0):
#         total+=number
# print(total)        
# for number in range(2,101,2):
#     total+=number
    
# print(total)


#Write your code below this row 👇
# for num in range(1,101):
#     if(num%5==0 & num%3==0):
#         print("FizzBuzz")
#     elif(num%5==0):
#         print("Buzz")
#     elif(num%3==0):
#         print("Fizz")
#     else:
#         print(num)    
        


