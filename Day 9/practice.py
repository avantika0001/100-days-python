#dictionaries and nesting

 ##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
#   Function: "A piece of code that you can easily call over and over again.",##ERROR because python will think that function is a variable declared somewhere if we don't use " "
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
#programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
#empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
#programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key) #prints only key not the value
#   print(programming_dictionary[key]) #key+value

#######################################

#Nesting 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

#Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

#Nesting Dictionary in a Dictionary as value to a key

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

#Nesting Dictionary in a List

# travel_log = [
#   {
#     "country": "France", 
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#   },
#   {
#     "country": "Germany", 
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#     "total_visits": 5
#   },
# ]



####################CODING EXERCISE
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades={}

# #TODO-2: Write your code below to add the grades to student_grades.👇

# for student in student_scores:
#     if(student_scores[student]<=70):
#         student_grades[student]="Fail"
#     elif student_scores[student]>71 and student_scores[student]<=80:
#         student_grades[student]="Acceptable"
#     elif student_scores[student]>80 and student_scores[student]<=90:
#         student_grades[student]="Exceeds Expectations"
#     elif student_scores[student]>90 and student_scores[student]<=100:
#         student_grades[student]="Outstanding"
#     else:
#         student_grades[student]="Not valid marks!"
             
# # 🚨 Don't change the code below 👇
# print(student_grades)

###########Coding Exercise
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_country(count):
    travel_log=travel_log.append({})





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)









