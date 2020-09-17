#!/usr/bin/env python3
import requests
import os

# Upload files in given directory using
# The Python Requests module

# Images are stored on image directory
direc = 'supplier-data/images/'
  
# Get list of files in image dir
files = os.listdir(direc)

#Upload to localhost upload directory
url = "http://localhost/upload/"

#Read each file from list
for file in files:
    if os.path.isfile(os.path.join(direc,file)):
        f, e = os.path.splitext(file)
        # only upload JPEG files
        outfile = f + ".jpeg"
        # if file is not a JPEG image file print message with filename
        if file == outfile:
            try:
                with open((os.path.join(direc,file)), 'rb') as opened:
                    r = requests.post(url, files={'file': opened})
		
            except OSError:
                print("Will not Upload", file)





