import pickle
import os
from pathlib import Path
import pandas as pd

class Word():
    def __init__(self, word_in_english = str(), word_in_norwegian = str()):
        
        self.word_in_english = word_in_english
        self.word_in_norwegian = word_in_norwegian
        self.times_answered = 0
        self.times_answered_correctly = 0
        self.id = 1 #needs work

    def ListOfWords():
        try:
            listdir = os.listdir()
            
    def AddWord():
        try:
            os.system('cls')
            print("Type the word in English:")
            new_word_eng = input()
            os.system('cls')
            print("Type the word in Norwegian:")
            new_word_no = input()

                if
                new_word = Word(new_word_eng, new_word_no)