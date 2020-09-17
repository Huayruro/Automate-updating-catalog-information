#!/usr/bin/env python3
import os
from PIL import Image
# Images are stored on image directory direc = 'supplier-data/images/'
direc = 'supplier-data/images/'
# The images received are in the wrong format: Size: Change image
# resolution from 3000x2000 to 600x400 pixel Format: Change image format
# from .TIFF to .JPEG After processing the images, save them in the same
# path

# Get list of files in image dir
files = os.listdir(direc)
#print(files)
# Change format of each image
for file in files:
    if os.path.isfile(os.path.join(direc,file)):
        f, e = os.path.splitext(file)
        #if you want to add extension to new file use outfile when
        #saving
        outfile = f + ".jpeg"
        # if file is not an image file print message with filename
        if file != outfile:
            try:
                with Image.open(os.path.join(direc,file)) as im:
                    im.resize((600,400)).convert('RGB').save(os.path.join(direc,outfile), 'JPEG')
            except OSError:
                print("cannot convert", file)
