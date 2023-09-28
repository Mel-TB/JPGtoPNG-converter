import os
import sys
from PIL import Image

# grab first and second argument using CLI
input_folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new_folder exist, if not create
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
else:
    print(f'The folder {new_folder} already exist. Give a new name')

# loop through images and convert to png (input_folder, new_folder, output_format='PNG'):
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(new_folder, filename.split('.')[0] + f'.png')

    img = Image.open(input_path)
    # save to new folder
    img.save(output_path)
print(f'Images are now converted and saved into {new_folder}.')
