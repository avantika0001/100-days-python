import random
from hangman_words import word_list
from hangman_art import logo,stages

lives=6
chosen_word = random.choice(word_list)
end_of_game=False

print(logo)
display=[]
for i in range(len(chosen_word)):
    display+="_"
    print(display[i], end =" ")


while end_of_game==False:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print("You've already guessed {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i]=guess
        print(display[i], end =" ") 

    if guess not in chosen_word:
        print(f"\nYou've guessed {guess}, that's not in the word. You lose a life!")
        lives-=1 
        if(lives==0):
            end_of_game=True
            print("You Lose!")    

    if "_" not in display:
        end_of_game=True
        print("You Win!")
    print(stages[lives])
      
    
            

