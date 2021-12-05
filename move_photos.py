import os
import shutil
import pandas as pd
import time
from send2trash import send2trash

start_time = time.time()
photos_path = r"D:\Photos"
keepers_path = r"D:\Photos\Keepers"
file_prefix = "DSC_"
file_suffixes = [".JPG", ".NEF", ".MOV"]

delimeters = [";", ","]

#  prefixing with "r" produces a raw string
temp_descriptions_path = r"D:\Photos\Keepers\test_2021-12-05\descriptions.xlsx"
temp_initial_path = temp_descriptions_path.replace(
    "Keepers\\", "").replace("descriptions.xlsx", "")
temp_destination_path = temp_descriptions_path.replace("descriptions.xlsx", "")

# Need path to descriptions.ods in keepers
# Need the name of new_keepers_folder from prev flow


def read_sheet(descriptions_path):
    descriptions_df = pd.read_excel(descriptions_path)
    print(descriptions_df.head())

    file_names_to_move = []

    for index, row in descriptions_df.iterrows():
        photo_nums_str = row['Photo Numbers']

        # Q: NaN is a float for some reason - WHY?
        if not isinstance(photo_nums_str, float):
            # QUESTION: What is the diff between an iterator and a list?
            # I think of these both as arrays
            photo_nums = list(
                filter(None, str(photo_nums_str).replace(",", ";").split(";")))

            # Create 4 digit value for each num b/c thats the file format
            for i, photo_num in enumerate(photo_nums):
                # Prepend the 0s in the file name
                tmp = "000" + photo_num
                # Keep only last 4 chars
                # list[start_bound: ending_bound]
                file_num = "".join(list(tmp)[-4:])
                file_name = file_prefix + file_num

                for j, file_suffix in enumerate(file_suffixes):
                    potential_file = file_name + file_suffix
                    file_in_path = temp_initial_path + potential_file
                    if(os.path.isfile(file_in_path)):
                        file_names_to_move.append(potential_file)
    return file_names_to_move


def move_photos(files):
    num_moved = 0
    # For each file_names_to_move, try to move each kind of file
    for i, file_name_to_move in enumerate(files):
        file_in_path = temp_initial_path + file_name_to_move
        if(os.path.isfile(file_in_path)):
            shutil.move(file_in_path, temp_destination_path)
            print(
                f"Moving: {file_in_path} {i+1}/{len(files)}", end="\r")
            num_moved += 1
    print(f"\nMoved: {num_moved} files")


def delete_nef_files(path):
    files = os.listdir(path)
    nef_counter = 0
    num_deleted = 0
    files_to_delete = []
    for file in files:
        if file.endswith('.NEF'):
            nef_counter += 1
            files_to_delete.append(file)

    for i, f in enumerate(files_to_delete):
        if not os.path.isdir(f) and ".NEF" in f:
            print(
                f"Deleting: {f} {i+1}/{nef_counter} .NEF files", end="\r")
            send2trash(path + f)
            num_deleted += 1
    print(f"\nDeleted: {num_deleted} files to Recycling Bin")


files_to_move = read_sheet(temp_descriptions_path)
move_photos(files_to_move)
delete_nef_files(temp_initial_path)
print("\nDone!")
print("--- %s seconds ---" % (time.time() - start_time))

# TODO: Figure out sleep from new_folder.py
# TODO: Check if all iNat paths are unique - Send warning if not
# TODO: Create an intializer function that creates a config file for
# specific paths for camera path and photos path
# TODO: Allow for ranges of photo nums
