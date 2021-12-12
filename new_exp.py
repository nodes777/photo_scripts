import new_folder
import move_photos
import sys

descriptions_file = new_folder.create_new_expedition(sys.argv[1])
print("Ready to move photos per the sheet? (y/n)")
my_input = input()
if my_input == "y":
    print("Moving photos...")
    print(descriptions_file)
    move_photos.sort_photos(descriptions_file)
if my_input == "n":
    print("Ok here's the file path for later")
    print(descriptions_file)


# TODO: Check if all iNat paths are unique - Send warning if not
# TODO: Create an intializer function that creates a config file for
# specific paths for camera path and photos path
# TODO: Allow for ranges of photo nums
