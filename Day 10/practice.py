#function with outputs
'''new things in this  tutorial
.title()
'''
def format_name(f_name,l_name):
    ###Docstrings###
    '''Take a first and last name and format it to return the title case version of the name.'''
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

string=format_name("avantika","PANDEY")
print(string)
output_f=len("avantika")


# #####CODING CHALLENGE
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year,month):
#   '''Shows number of days in a specific     #   month in a year'''
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   ###DOUBT
#   if(is_leap(year) and month==2):
#     month_days[month-1]+=1
#   return month_days[month-1]
   
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)





