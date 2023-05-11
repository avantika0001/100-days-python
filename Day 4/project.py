rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices=[rock,paper,scissors]
computer_choice=random.randint(0,2)
user_choice=int(input("Enter your choice, 0=rock, 1=paper, 2=scissors: "))
print(f"You chose{choices[user_choice]}")
print(f"Computer chose{choices[computer_choice]}")
if(user_choice==computer_choice):
    print("It's a draw! Try again!")
elif(user_choice==0 and computer_choice==1):
    print("You lose")
elif(user_choice==0 and computer_choice==2):
    print("You Win")    
elif(user_choice==1 and computer_choice==2):
    print("You Lose!")
elif(user_choice==1 and computer_choice==0):
    print("You Win!")
elif(user_choice==2 and computer_choice==0):
    print("You Lose!")
elif(user_choice==2 and computer_choice==1):
    print("You Win!")             

