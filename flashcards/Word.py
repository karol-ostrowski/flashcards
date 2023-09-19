import os
import pandas as pd

def AddWord():
        if not os.path.exists('words.csv'):
            with open('words.csv', 'w') as file:
                file.write("word in norwegian,word in english,times answered,times answered correctly")
        
        os.system('cls')
        df_words = pd.read_csv('words.csv')
        word_in_norwegian = input("adding a word\ntype the word in norwegian: ")
        os.system('cls')
        word_in_english = input("adding a word\ntype the word in english: ")
        os.system('cls')
        new_word = {'word in norwegian' : word_in_norwegian, 'word in english' : word_in_english, 'times answered' : 0, 'times answered correctly' : 0}
        df_words.loc[len(df_words)] = new_word
        df_words.to_csv('words.csv', index=False)

def GetListOfWords():
    if not os.path.exists('words.csv'):
        input("database of words is empty, press enter to continue ")
    else:
         df_words = pd.read_csv('words.csv')
         print(df_words)