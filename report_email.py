#!/usr/bin/env python3
import os
import reports
import emails

from datetime import datetime

def main():
  #  date in format Month day, year
  today = datetime.today().strftime("%B %d, %Y")  

  # Pdf file created
  attachment= "/tmp/processed.pdf"

  # Pdf Title
  title = "Processed Update on {}".format(today)

  # Uses the info stored in this folder
  dire="supplier-data/descriptions/"

  # returns a list of all files and directories in the specified path
  files = os.listdir(dire)
  # 2 blank lines
  body="<br/><br/>"
  # Generates PDF body with each detail processed
  for file in files:
    try:
      with open(os.path.join(dire,file), mode='r',encoding='UTF-8') as feed:
        i=0
        for line in feed.readlines():
              #first line is name
              if i==0:
                body+="name: "
                body+=line.rstrip()
                body+="<br/>"
              #second line is weight
              if i==1:
                body+="weight: "
                body+=line.rstrip()
                body+="<br/>"
              i+=1
      body+="<br/>"
    except:
        print("Error reading", os.path.join(dire,file))
  paragraph=body
  #Build the PDF
  reports.generate_report(attachment, title, paragraph)
  #Sends email
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)


if __name__ == "__main__":
  main()
