#!/usr/bin/env python
import shutil
import psutil
import requests
import socket
import os
import time
import emails

def check_cpu_usage():
    # Returns an error if CPU usage is over 80%
    usage=psutil.cpu_percent(1)
    return usage<=80

def check_disk_usage(disk):
    # Returns an error if available disk space is lower than 20%
    du=shutil.disk_usage(disk)
    free =du.free / du.total*100
    return free>20

def check_memory():
    # Returns an error if available memory is less than 500MB 
    avail=(psutil.virtual_memory().available)
    return avail>500

def check_localhost():
    # Returns an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
    localhost = socket.gethostbyname('localhost')
    return localhost=="127.0.0.1"


starttime = time.time()
# email info
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

# Checks system statistics: CPU usage, disk space, available memory and name resolution
while True:
    if not check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)
    elif not check_disk_usage("/"):
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)
    elif not check_memory():
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)
    elif not check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)
    # Checks every 60 seconds
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
