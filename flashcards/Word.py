import os
import pandas as pd
import time

def AddWord():
        if not os.path.exists('words.csv') or pd.read_csv('words.csv').shape[0] == 0:
            with open('words.csv', 'w') as file:
                file.write("word in norwegian,word in english,times answered,times answered correctly")

        df_words = pd.read_csv('words.csv')
        word_in_norwegian = input("adding a word\ntype the word in norwegian: ")
        os.system('cls')
    
        if word_in_norwegian in df_words['word in norwegian'].values:
             input("word already exists in the database, press enter to continue ")
             return
        
        word_in_english = input("adding a word\ntype the word in english: ")
        os.system('cls')
        new_word = {'word in norwegian' : word_in_norwegian, 'word in english' : word_in_english, 'times answered' : 0, 'times answered correctly' : 0}
        df_words.loc[len(df_words)] = new_word
        df_words.to_csv('words.csv', index=False)

def EditOrRemove():
    try:
        df_words = pd.read_csv('words.csv')
    except:
        input("database is empty or doesnt exist, press enter to continue...")
        return
    loopin = 0
    while loopin < 1:
        word_to_edit_or_remove = input("which word do you want to edit/remove?\ntype 'show list' to check the list of existing words or 'exit' to exit\n")

        if word_to_edit_or_remove == 'show list':
            GetListOfWords()
        elif word_to_edit_or_remove == 'exit':
            break
        elif word_to_edit_or_remove in df_words['word in norwegian'].values:
            while True:
                os.system('cls')
                edit_or_remove = input("1 - edit\n2 - remove\n")
                if edit_or_remove == '1':   #editing
                    os.system('cls')
                    edited_word_in_norwegian = input("new spelling of the word in norwegian:\n")
                    os.system('cls')
                    edited_word_in_english = input("new spelling of the word in english:\n")
                    df_words.loc[df_words[df_words['word in norwegian'] == word_to_edit_or_remove].index, ['word in norwegian', 'word in english']] = edited_word_in_norwegian, edited_word_in_english

                    # df_words[df_words['word in norwegian'] == word_to_edit_or_remove].index -> this code returns the index of a row with a value corresponding to given value, seems like an useful thing

                    df_words.to_csv('words.csv', index=False)
                    loopin = 1
                    break
                elif edit_or_remove == '2':     #removing
                    os.system('cls')
                    df_words.drop(df_words[df_words['word in norwegian'] == word_to_edit_or_remove].index, inplace=True) #doesnt delete chosen word, i think this line is a problem
                    df_words.to_csv('words.csv', index=False)
                    input(f"removed {word_to_edit_or_remove}, press enter to continue...")
                    loopin = 1
                    break
                else:
                    os.system('cls')
                    print("wrong input")
                    time.sleep(2)

        else:
            os.system('cls')
            input("word doesnt exist in the database, press enter to continue... ")

def GetListOfWords():

    if not os.path.exists('words.csv') or os.path.getsize == 0:
        input("database of words is empty, press enter to continue ")
    else:
        df_words = pd.read_csv('words.csv')
        if df_words.shape[0] == 0:
            input("database is empty, press enter to continue...")
        else:
            print(df_words)
            input('press enter to continue...')
        