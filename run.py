#!/usr/bin/env python3
import os
import requests
# Uploads all the info stored in this folder to the company's website
dire="supplier-data/descriptions/"
# company's website fruit catalog web-server url
url = 'http://34.123.229.55/fruits/'

# keys for the content value
headers=["name", "weight", "description", "image_name"]

# returns a list of all files and directories in the specified path
files = os.listdir(dire)
# Sorts files so they will upload in order
files=sorted(files)

for file in files:

  if os.path.isfile(os.path.join(dire,file)):
    f, e = os.path.splitext(file)
    # image name
    image = f + ".jpeg"

    try:
      with open(os.path.join(dire,file), mode='r',encoding='UTF-8') as feed:
        #initialize counter for headers and dictionary
        i=0
        diccio={}
        for line in feed.readlines():
          # The weight field is defined as an integer field. 
          # Split the line & Convert it into an integer
          if i==1:
            num, unit = line.split()
            line1=int(num)
            diccio[headers[i]]=line1
          else:
            diccio[headers[i]]=line	
          i+=1
        #add image name
        diccio[headers[3]]=image
        # post the dictionary to the company's website.
        x = requests.post(url=url, data = diccio)
        #check if posting was succesfull
        if x.status_code==201:
          print("Success posting ",file)
        else:
          print("Error posting ",file)
    except:
        print("Error reading", os.path.join(dire,file))
