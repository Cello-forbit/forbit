

import colorama
from colorama import init, Fore, Back, Style

init(convert=True)
import colorama
import random
import pyfiglet 


def making_a_guess():
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    if correct_guess == False:
        print(f"det finns ingen {guess}, försök igen.")
        update_display += 1
    x = 0

 
 
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
 
word_list = ["kanin", "apa", "kamel", "rock", "träd", "fisk", "slott", "måne"]
 
chosen_word = list(random.choice(word_list))
 
blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)
 
update_display = 0

#----------------------------------------------------------------------------------------------
 

print(HANGMANPICS[update_display])
print("välkommen till hängagubbe python edition.")

print("ordet har")
print(len(chosen_word))
print("bokstäver")
print("gissa en bokstav")
guess = input("")
making_a_guess()
print(HANGMANPICS[update_display])
print(''.join(blank_list))
while update_display < 6:
    if blank_list == chosen_word:
        print(Fore.GREEN + pyfiglet.figlet_format("BRA JOBBAT, ", font="speed" ))
        print(Fore.BLUE + pyfiglet.figlet_format("DU ÖVERLEVDE!", font="speed" ))
        break
    guess = input("Gissa en gång till ")
    making_a_guess()
    print(HANGMANPICS[update_display])


    print(''.join(blank_list))
if update_display == 6:
 print (Fore.RED+Style.BRIGHT + pyfiglet.figlet_format("sorry,"))
 print (Fore.RED+Style.BRIGHT + pyfiglet.figlet_format( "DU BLEV HÄNGD!" ))
 print (Fore.RED+Style.BRIGHT + pyfiglet.figlet_format( "och nu är du död..." ))
print("ordet var")
print(chosen_word)
print("prova igen!")