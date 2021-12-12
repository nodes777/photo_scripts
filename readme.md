# Photo Script Mover

This is a collection of python scripts that help me manage my photos after returning from an "expedition".

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these dependencies:

- Path
- Datetime
- Numpy
- Pandas

## Usage

`new_exp.py <name_of_location_of_expedition>`

When prompted with `"Ready to move photos per the sheet? (y/n)"`

Entering `y` will move keeper photos and delete unmoved .NEF files.
Entering `n` prints the path of the new description spreadsheet and ends the program

You can put this folder `\photo_scripts\` in your PATH so that you can just do `new_exp.py <name_of_location_of_expedition>` in the terminal.

### Sub functions

`python3 new_folder.py <name_of_location_of_expedition>`

After replacing the path of the new descriptions.xlsx in `temp_descriptions_path` in `move_photos.py`:

`python3 move_photos.py`

## `new_folder.py`

- Creates new folder in `D:\Photos\<name_from_arguement>_<current_date>` and in `D:\Photos\Keepers\<name_from_arguement>_<current_date>`
- Copies a descriptions.xlsx template and places it in the new keepers folder path
- Moves photos from the camera to the photos folder

## `move_photos.py`

- Reads the descriptions.xlsx of the keepers folder to determine which photos will move
- Moves all photo numbers that match the numbers in the xlsx (".JPG", ".NEF", ".MOV")
- Deletes all ".NEF" files that have not been moved to the new keepers folder

## License

[MIT](https://choosealicense.com/licenses/mit/)
