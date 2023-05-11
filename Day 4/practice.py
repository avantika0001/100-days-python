#randomisation, lists
#Mersene twister
#pseudo random num generator

import random
# import my_module

# random_integer=random.randint(1,10)
# print(random_integer)
# print(my_module.pi)

# #0-0.99999...
# random_float =random.random()
# print(random_float)
# #0-4.9999...
# print(random_float*5)

# love_score=random.randint(1,100)
# print(f"your love score is {love_score}")

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

# toss_result=random.randint(0,1)
# #print(toss_result)
# if toss_result==0:
#     print("Tails")
# if toss_result==1:
#     print("Heads")    

#random.seed(123)

"""Python Lists"""

# states_of_india = ["Haryana", "Maharashtra", "Bihar"]

# print(states_of_india)          # ['Haryana', 'Maharashtra', 'Bihar']

# print(states_of_india[0])       # Haryana
# print(states_of_india[1])       # Maharashtra
# print(states_of_india[2])       # Bihar

# print(states_of_india[-1])      # Bihar

# states_of_india[0] = "Jammu and Kashmir"
# print(states_of_india)           # ['Jammu and Kashmir', 'Maharashtra', 'Bihar']

# states_of_india.append("Punjab")
# print(states_of_india)          # ['Jammu and Kashmir', 'Maharashtra', 'Bihar', 'Punjab']

# states_of_india.extend(["Mizoram", "Meghalaya"])
# print(states_of_india)          # ['Jammu and Kashmir', 'Maharashtra', 'Bihar', 'Punjab', 'Mizoram', 'Meghalaya']

# 0 1 2 offset from begining so numbering in this format

# """Who's Paying Exercise"""
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# print(names)
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# payer=random.randint(0,len(names)-1)
# print(names[payer])
# can be done by random.choice



"""Nested Lists"""

# dirty_dozen = ["strawberries", "celery", "apples", "cherries", "potato" ,"spinach"]
# print(dirty_dozen)

# fruits = ["strawberries", "apples", "cherries"]
# vegetables = ["celery", "potato", "spinach"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

"""Treasure Island Exercise"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") #colrow
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

desired_row=map[int(position[1])-1]
desired_row[int(position[0])-1]='X'
#map[int(position[1])-1][int(position[0])-1]="X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")



