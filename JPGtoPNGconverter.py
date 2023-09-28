# Create PNG converter file
# Need to add folder and create new folder
# images\ new\

import os
import sys
from PIL import Image

# grab first and second argument
input_folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new\ exist, if not create
if not os.path.exists(new_folder):
    os.mkdir(new_folder)

# loop through images and convert to png (input_folder, new_folder, ouput_format='PNG'):

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(new_folder, filename.split('.')[0] + f'.png')

        img = Image.open(input_path)
        # save to new folder
        img.save(output_path)
