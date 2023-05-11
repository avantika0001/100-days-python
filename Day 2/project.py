#tip calculator

print("Welcome to the tip claculator.")
bill=float(input("What was the total bill? $"))
per=int(input("How much tip would you like to give? 10, 12, or 15? "))
num=int(input("How many people to split the bill? "))
final_bill=(bill+bill*(per/100))/num
each_pay=round(final_bill,2)
print(each_pay)