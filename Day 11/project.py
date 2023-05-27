############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from art import logo
import os
os.system("cls")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    while_play=True
    while while_play:     
        print(logo)
        dealer_choice=random.choices(cards,k=2)
        user_choice=random.choices(cards,k=2)
        print(f"Your cards: {user_choice}")
        print(f"Computer's first card: {dealer_choice[0]}")
        if(sum(user_choice)>21):
            print("Sum over 21! Game over!")
            exit()
        if input("Type 'y' to get another card, type 'n' to pass: ")=='y':
            user_choice.append(random.choice(cards))
            print(f"Your final hand: {user_choice}")
        if(sum(user_choice)>21):
            print("Sum over 21! Game over!")
        elif sum(user_choice)>sum(dealer_choice):
            print("You win!!")
        else:
            print("You lose!")
            print(f"Computer's cards were: {dealer_choice}")   

        if input("Do you want to play a game of blackjack? type 'y' or 'n': ")=='y':
            os.system("cls")
            blackjack()
        else:
            while_play=False

#calling main function
blackjack()
#alternate solution: https://replit.com/@appbrewery/blackjack-final#main.py

