'''Debugging'''

############TIPS FOR DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): ####bug (1,21)####
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) ####bug (0,5)####
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:  ####bug year=>1994####
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") ####bugs: indent,int convert,f string####
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) ####bug:"="####
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger :https://pythontutor.com/visualize.html#mode=display 
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) ####bug:indent this line####
#   print(b_list)

# mutate([1,2,3,5,8,13])

############coding exercise

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:  ##bug ==
#   print("This is an even number.")
# else:
#   print("This is an odd number.")





