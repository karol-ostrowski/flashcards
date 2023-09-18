#app written because i don't think i like any existing flashcard app

import os
from pathlib import Path
#import Word


current_path = os.getcwd()
words_folder_path = os.path.join(current_path, 'words')
print(words_folder_path)

if os.path.exists(words_folder_path) and os.path.isdir(words_folder_path):
    for file in os.listdir(words_folder_path):
        print(file)
else:
    os.makedirs(words_folder_path)


#note to self: czy jak zimportuje obiekt ktory ma zimporotwany modul to on tez bedzie zimportowany