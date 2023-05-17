#ceaser cipher
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
list1 = list(text)

shift=shift%25

def caesar(text,shift_i,direction):
    end_text=""
    if direction=="decode":
            shift_i *= -1
    for letter in text:
        if letter in alphabet: 
            position=alphabet.index(letter) 
            new_position=position+shift_i
            end_text+=alphabet[new_position]
        else:
            end_text+=letter    
    print(f"The {direction}d text is {end_text}") 

caesar(text,shift,direction)
 
