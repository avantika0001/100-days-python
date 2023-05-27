#Number guessing game!
import random 
import art

final_num=random.randint(1,100)

def game_logic(attempts_left,play_game):
    while play_game:
        if attempts_left==0:
            print("You lost your number of attempts!")
            print(art.logo3)
            play_game=False
        else:
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))
            if guess>final_num:
                print("Too High")
                attempts_left-=1
            elif guess < final_num:
                print("Too Low")
                attempts_left-=1 
            else:
                print("Correct guess!")
                print(art.logo2)
                play_game=False
    
print(art.logo)
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("I'm thinking of a number between 1 and 100.")
if input("Choose a difficulty. Type 'easy' or 'hard': ")=='easy':
    game_logic(attempts_left=10,play_game=True)
else:
    game_logic(attempts_left=5,play_game=True)                 

