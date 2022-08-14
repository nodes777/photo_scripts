import os
from datetime import datetime
import shutil
import time

# 102D7000 - Moms D7000
# 108D3400 - My Camera
camera_path = "E:/DCIM/108D3400"
photos_path = r"D:\Photos"
keepers_path = r"D:\Photos\Keepers"
descriptions_template_path = r"D:\Photos\Keepers\descriptions_template.xlsx"
descriptions_file_name = "descriptions.xlsx"
todays_date = datetime.today().strftime('%Y-%m-%d')

MissingInputError = "Error No Folder Name Provided"


def make_new_folder(folder_name_input):
    if(folder_name_input is None):
        raise MissingInputError()
    new_folder_name = folder_name_input + "_" + todays_date
    new_folder = os.path.join(photos_path, new_folder_name)
    os.makedirs(new_folder, exist_ok=False)
    print(f'Created New Folder {new_folder}')
    return new_folder, new_folder_name


def move_photos_from_camera_to_comp(camera_path, new_folder):
    files_on_camera = os.listdir(camera_path)
    num_of_files = len(files_on_camera)
    # TODO: If moving files fails, delete the new_folder that was created
    for idx, file in enumerate(files_on_camera):
        shutil.move(camera_path + "/" + file, new_folder)
        # end="\r" print to start where last one ended, clears terminal line
        print(f"Moving {file} {idx}/{num_of_files}", end="\r")


def create_keepers_folder(new_folder_name):
    # Create the same folder name, under /Keepers
    new_keepers_folder = os.path.join(keepers_path, new_folder_name)

    os.makedirs(new_keepers_folder, exist_ok=False)
    print(f'Created New Folder {new_keepers_folder}')
    # Copy a descriptions file from template
    descriptions_copy = shutil.copy(
        descriptions_template_path, new_keepers_folder)
    # Remove the "template" part of the name
    descriptions_file = new_keepers_folder + "\\" + descriptions_file_name
    os.rename(descriptions_copy, descriptions_file)
    os.startfile(descriptions_file)
    os.startfile(new_keepers_folder)
    return descriptions_file


def create_new_expedition(folder_name_input):
    start_time = time.time()
    new_folder, new_folder_name = make_new_folder(folder_name_input)
    move_photos_from_camera_to_comp(camera_path, new_folder)
    descriptions_file = create_keepers_folder(new_folder_name)
    print("--- %s seconds ---" % (time.time() - start_time))
    os.startfile(new_folder)
    return descriptions_file
