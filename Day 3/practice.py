#conditionals , logical operators, code blocks and scope

"""Control Flow"""

# print("Welcome to the roller coaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller to ride the roller coaster!")


# """Comparison operators"""
# # ==    -> Equals to   
# # >     -> Greater than
# # >=    -> Greater than or equals to
# # <     -> Less than
# # <=    -> Less than or equals to

# """Odd Even Exercise"""

# # # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # # 🚨 Don't change the code above 👆

# # #Write your code below this line 👇
# # 7%2 ans is the remainder modulo operator
# if number%2==0:
#     print("The number is even!")
# else:
#     print("The number is odd!")    

# # ## 👆

"""Nested if statement"""

# print("Welcome to the roller coaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("Enter your age? "))

#     if age <= 18:
#         print("Please pay $7")
#     else:
#         print("PLease pay $12")
# else:
#     print("Sorry, you have to grow taller to ride the roller coaster!")


"""elif Statement"""

# print("Welcome to the roller coaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("Enter your age? "))

#     if age < 12:
#         print("Please pay $5")

#     elif age <= 18:
#         print("Please pay $7")

#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller to ride the roller coaster!")


"""BMI Calculation 2.0 Exercise"""

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


### CODE ###

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bmi = round(weight / height**2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")

# elif bmi < 25 :
#     print(f"Your BMI is {bmi}, you have a normal weight")

# elif bmi < 30 :
#     print(f"Your BMI is {bmi}, you are slightly overweight")

# elif bmi < 35 :
#     print(f"Your BMI is {bmi}, you are obese")

# else :
#     print(f"Your BMI is {bmi}, you are clinically obese")

# ## 👆


"""Leap Year Exercise"""

# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 

# This is how you work out whether if a particular year is a leap year :
# 
# On every year that is evenly divisible by 4 **except** 
# every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400


### CODE ###

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# ## 👆



"""Multiple if Statements"""


# print("Welcome to the roller coaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("Enter your age? "))
#     bill = 0

#     if age < 12:
#         print("Child tickets are $5")
#         bill = 5
#     elif age <= 18:
#         print("Youth tickets are $7")
#         bill = 7

#     else:
#         print("Adult tickets are $12")
#         bill = 12

#     wants_photo = input("Do you want your photo taken for $3? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your total bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller to ride the roller coaster!")

"""Pizza Order Exercise"""

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1


### CODE ###

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L : ")
# add_pepperoni = input("Do you want pepperoni? Y or N : ")
# extra_cheese = input("Do you want extra cheese? Y or N : ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else :
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else: 
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# ## 👆

"""Logical Operators"""

# a = 15
# b = 7
# print( a>10 and b<100 )   # True
# print( a>5 and b<6 )      # False

# print( a>20 or b<5 )      # False
# print( a>5 or b<6 )       # False

# print( not a>10 )         # False
# print( not b<3 )          # True

# and  
# or
# not

"""Love Calculator Exaecise"""

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

### CODE ###

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1 + name2

combined_name = combined_name.lower()

true_count = 0
love_count = 0

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

true_count = t + r + u + e
love_count = l + o + v + e

love_score = int(str(true_count) + str(love_count))

if love_score < 10  or  love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")

## 👆