#app written because i don't think i like any existing flashcard app
import os
import Word
import time
import Game

while True:
    os.system('cls')
    menu_input = input("1 - play\n2 - add a word\n3 - check the list of words with statistics\n4 - edit or remove existing word\n5 - exit\n")
    if menu_input == '1':
        Game.Play()
    elif menu_input == '2':
        Word.AddWord()
    elif menu_input == '3':
        Word.GetListOfWords()
    elif menu_input == '4':
        Word.EditOrRemove()
    elif menu_input == '5':
        break
    else:
        os.system('cls')
        print("wrong input")
        time.sleep(2)