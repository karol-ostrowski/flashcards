#app written because i don't think i like any existing flashcard app

import os
from pathlib import Path
#import Word


current_path = os.getcwd()
words_folder_path = os.path.join(current_path + 'words')

with open(words_folder_path, 'r') as f:
    list = os.listdir()
    for file in list:
        print(file)

#note to self: czy jak zimportuje obiekt ktory ma zimporotwany modul to on tez bedzie zimportowany
#asdsdasdllsss
