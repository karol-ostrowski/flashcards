import Word
import os
import pandas as pd
import time

def gamemode(df_words, questions, answers, number_of_rounds, gamemode):
    index = 0
    correct_answers = 0
    while index <= int(number_of_rounds) - 1:
        question = questions.iloc[index]
        answer = answers.iloc[index]
        if gamemode == '1':
            word_in_norwegian = question
        else:
            word_in_norwegian = answer
        
        os.system('cls')
        user_answer = input(f"round {index + 1}/{number_of_rounds}\n{question} = ...\n")

        if user_answer == answer:
            df_words.loc[df_words['word in norwegian'] == word_in_norwegian, ['times answered', 'times answered correctly']] = \
                int(df_words['times answered'][df_words[df_words['word in norwegian'] == word_in_norwegian].index]) + 1,\
                int(df_words['times answered correctly'][df_words[df_words['word in norwegian'] == word_in_norwegian].index]) + 1
            correct_answers += 1

        else:
            df_words.loc[df_words['word in norwegian'] == word_in_norwegian, ['times answered']] = \
            [int(df_words['times answered'][df_words[df_words['word in norwegian'] == word_in_norwegian].index]) + 1]

        index += 1
    os.system('cls')
    input(f"you correctly answered {correct_answers} times out of {number_of_rounds}\npress enter to continue...")

    df_words.to_csv('words.csv', index=False)
        

def Play():
    if not os.path.exists('words.csv') or os.path.getsize == 0:
        input("database of words is empty, press enter to continue ")
    else:
        df_words = pd.read_csv('words.csv')
        if df_words.shape[0] == 0:
            input("database is empty, press enter to continue...")
    
    os.system('cls')
    df_words = pd.read_csv('words.csv')
    game_mode = input("1 - no -> eng\n2 - eng -> no\n")
    os.system('cls')
    try:
        number_of_questions = int(input("how many words do you want to be asked?\n"))
    except:
        print("error occured")
    
    if number_of_questions > df_words.index[-1] + 1:
        print(f"there are only {df_words.index[-1]+1} words in the database\nyou will be asked {df_words.index[-1]+1} words")
        number_of_questions = df_words.index[-1]+1
        time.sleep(2)

    df_words_shuffled = df_words.sample(n=number_of_questions)
    no = df_words_shuffled['word in norwegian']
    eng = df_words_shuffled['word in english']

    while True:
        if game_mode == '1':
            gamemode(df_words, no, eng, number_of_questions, game_mode)
            break
        elif game_mode == '2':
            gamemode(df_words, eng, no, number_of_questions, game_mode)
            break
        else:
            print("wrong input")
            break
