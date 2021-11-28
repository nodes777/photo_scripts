import os
import sys
import re
from pathlib import Path
import shutil
import numpy as np
import pandas as pd


photos_path = "D:\Photos"
keepers_path = "D:\Photos\Keepers"
descriptions_template_path = "D:\Photos\Keepers\descriptions_template.ods"

# DSC_0001.JPG

file_prefix = "DSC_"
file_suffixes = [".JPG",".NEF",".MOV"]
delimeters = [";",","]

temp_descriptions_path = "D:\Photos\Keepers\La_Perouse_2021-11-14\descriptions_template.xlsx"
temp_initial_path = temp_descriptions_path.replace("Keepers\\","").replace("descriptions_template.xlsx","")
temp_destination_path = temp_descriptions_path.replace("descriptions_template.xlsx","")

# Need path to descriptions.ods in keepers
# Need the name of new_keepers_folder from prev flow

descriptions_df = pd.read_excel(temp_descriptions_path)
print(descriptions_df.head())

file_names_to_move = []
    
# Loop through each row
# For the text in each Photo Numbers
# Take each number per delimiter
for index, row in descriptions_df.iterrows():
    photo_nums_str = row['Photo Numbers']

    # Q: NaN is a float for some reason - WHY?
    if not isinstance(photo_nums_str, float):
        # QUESTION: Why isnt this splitting on the ;?
        # photo_nums = re.split('; |,', photo_nums_str)

        # replace then split b/c above doesn't work
        # filter does a filter, returns an iterator, list() puts it in a list
        # QUESTION: What is the diff between an iterator and a list? - I think of these both as arrays
        photo_nums = list(filter(None, photo_nums_str.replace(",",";").split(";")))

        # Create 4 digit value for each num b/c thats the file format
        # Q: Is there a better way to match the file names to the nums?

        for i, photo_num in enumerate(photo_nums):
            # Prepend the  0s in the file name
            tmp =  "000" + photo_num
            # Keep only last 4 chars
            # list[start_bound: ending_bound]
            file_num = "".join(list(tmp)[-4:])
            file_name = file_prefix + file_num
            # TODO sometimes .NEF files or .MOV files won't exist. 
            # Should I add them here or do logic to filter somewhere before trying to move
            file_names_to_move.append(file_name + ".JPG")
            file_names_to_move.append(file_name + ".NEF")
            file_names_to_move.append(file_name + ".MOV")


# For each file_names_to_move, try to move each kind of file
for idx, file_name_to_move in enumerate(file_names_to_move):
    file_in_path = temp_initial_path + file_name_to_move 
    if(os.path.isfile(file_in_path)):
        shutil.move(file_in_path, temp_destination_path)
        # end="\r" print to start where previous one ended, to remove previous line in terminal
        print(f"Moving {file_in_path} {idx}/{round(len(file_names_to_move)-1/2)}", end="\r")

print("\n Done!")

# TODO: Put these into functions
# TODO: Figure out sleep from new_folder.py
# TODO: Delete NEF files that aren't moved
# TODO: Check if all iNat paths are unique - Send warning if not
# TODO: Create an intializer function that creates a config file for specific paths for camera path and photos path
# TODO: Rename the descriptions_template.xlsx to just descriptions