# #data types, numbers, operations, type conversions, f-strings

# #data types

# #string
# print("hello"[2])

# print("123"+"345") #concatenation

# #integer

# print(123+345)

# 123_456_789

# #float 
# 3.1432

# #boolean 
# True
# False

# # we cant concatenate strings and integers
# num_char= len(input("type your name: "))
# #type-checking
# print(type(num_char))
# #type-conversion
# new_num_char=str(num_char)

# print("Your name has "+ new_num_char + " characters.")

# #Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# result=int(two_digit_number[0])+int(two_digit_number[1])
# print(result)

#mathematical operations
#PEMDASLR
#6/3 FLOAT result of divion is float

# #BMI CALCULATOR
# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# BMI= float(weight)/float(height)**2
# print("BMI: "+ str(int((BMI))))

#round
# print(round(8/3,2))
#8//3 ans:int 2 floor division

#f strings
# player_name="avantika"
# score=10
# height=1.8
# isWining=True
# print(f"{player_name}'s score is {score}, and their height is: {height}, they are winning is {isWining}")

#Life in weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days=(365*90)-(365*int(age))
weeks=(52*90)-(52*int(age))
months=(12*90)-(12*int(age))

print(f"You have {days} days, {weeks} weeks, and {months} months left.")