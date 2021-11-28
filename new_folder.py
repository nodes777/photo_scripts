import os
import sys
from datetime import datetime
from pathlib import Path
import shutil
import time

start_time = time.time()

camera_path = "E:/DCIM/108D3400"
photos_path = "D:\Photos"
keepers_path = "D:\Photos\Keepers"
descriptions_template_path = "D:\Photos\Keepers\descriptions_template.xlsx"
todays_date =  datetime.today().strftime('%Y-%m-%d')

MissingInputError = "Error No Folder Name Provided"

def make_new_folder(folder_name_input):
    if(folder_name_input == None):
        raise MissingInputError()
    new_folder_name = folder_name_input + "_" + todays_date
    new_folder = os.path.join(photos_path,new_folder_name)
    os.makedirs(new_folder,exist_ok=False)
    print(f'Created New Folder {new_folder}')
    return new_folder, new_folder_name

def move_photos_from_camera_to_comp(camera_path,new_folder):
    files_on_camera = os.listdir(camera_path)
    num_of_files = len(files_on_camera)
    # TODO: If the moving of files fails, delete the new_folder that was created
    for idx, file in enumerate(files_on_camera):
        shutil.move(camera_path + "/" + file, new_folder)
        # end="\r" print to start where previous one ended, to remove previous line in terminal
        print(f"Moving {file} {idx}/{num_of_files}", end="\r")
        

def create_keepers_folder(new_folder_name):
    # Create the same folder name, under /Keepers
    new_keepers_folder = os.path.join(keepers_path,new_folder_name)
    # TODO Rename descriptions_tempplate to descriptions

    os.makedirs(new_keepers_folder,exist_ok=False)
    print(f'Created New Folder {new_folder}') 
    # Copy a descriptions file from template
    descriptions_file = shutil.copy(descriptions_template_path,new_keepers_folder)
    os.startfile(descriptions_file)
    # TODO: open first image

    return descriptions_file



new_folder, new_folder_name = make_new_folder(sys.argv[1])

move_photos_from_camera_to_comp(camera_path, new_folder)

create_keepers_folder(new_folder_name)
print("--- %s seconds ---" % (time.time() - start_time))