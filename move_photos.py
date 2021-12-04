import os
import sys
import re
from pathlib import Path
import shutil
import numpy as np
import pandas as pd
import time

start_time = time.time()
photos_path = "D:\Photos"
keepers_path = "D:\Photos\Keepers"
file_prefix = "DSC_"
file_suffixes = [".JPG",".NEF",".MOV"]
delimeters = [";",","]

#  prefixing with "r" produces a raw string
temp_descriptions_path = r"D:\Photos\Keepers\bundeena_to_royal_national_park_2021-11-28\descriptions_template.xlsx"
temp_initial_path = temp_descriptions_path.replace("Keepers\\","").replace("descriptions_template.xlsx","")
temp_destination_path = temp_descriptions_path.replace("descriptions_template.xlsx","")

# Need path to descriptions.ods in keepers
# Need the name of new_keepers_folder from prev flow
def read_sheet_and_move_files(descriptions_path):
    descriptions_df = pd.read_excel(descriptions_path)
    print(descriptions_df.head())

    file_names_to_move = []
    
    for index, row in descriptions_df.iterrows():
        photo_nums_str = row['Photo Numbers']

        # Q: NaN is a float for some reason - WHY?
        if not isinstance(photo_nums_str, float):
            # QUESTION: What is the diff between an iterator and a list? - I think of these both as arrays
            photo_nums = list(filter(None,str(photo_nums_str).replace(",",";").split(";")))

            # Create 4 digit value for each num b/c thats the file format
            for i, photo_num in enumerate(photo_nums):
                # Prepend the 0s in the file name
                tmp =  "000" + photo_num
                # Keep only last 4 chars
                # list[start_bound: ending_bound]
                file_num = "".join(list(tmp)[-4:])
                file_name = file_prefix + file_num

                for j, file_suffix in enumerate(file_suffixes):
                    file_names_to_move.append(file_name + file_suffix)
                    
    # For each file_names_to_move, try to move each kind of file
    for idx, file_name_to_move in enumerate(file_names_to_move):
        file_in_path = temp_initial_path + file_name_to_move 
        if(os.path.isfile(file_in_path)):
            shutil.move(file_in_path, temp_destination_path)
            # end="\r" print to start where previous one ended, to remove previous line in terminal
            print(f"Moving {file_in_path} {idx}/{round(len(file_names_to_move)-1/2)}", end="\r")

read_sheet_and_move_files(temp_descriptions_path)
print("\n Done!")
print("--- %s seconds ---" % (time.time() - start_time))

# TODO: Figure out sleep from new_folder.py
# TODO: Delete NEF files that aren't moved
# TODO: Check if all iNat paths are unique - Send warning if not
# TODO: Create an intializer function that creates a config file for specific paths for camera path and photos path
# TODO: Allow for ranges of photo nums
