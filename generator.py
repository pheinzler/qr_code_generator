# Importing library
import qrcode
import datetime
import os
import random
import yaml

# setup things for naming of fils/folders
random.seed(None, 2)
date = datetime.date.isoformat(datetime.date.today())

#open yaml config and get config data
with open('config.yml', 'r') as file:
    prime_service = yaml.safe_load(file)

DATA = prime_service["config"]["data"]
FILENAME = prime_service["config"]["filename"]

# check for correct data and filename
if(DATA == ""):
    print("No argmuent given. Please specify DATA argument in config.yml to generate qr Code")
    exit()
if(FILENAME == ""):
    FILENAME = date + str(random.randint(0,1000))

# Encoding data using make() function
img = qrcode.make(DATA)

#create folder for qr_codes
try:
    os.mkdir("qr_codes/"+ date)
except:
    None
#create path
path= "qr_codes/"+date+"/"

# Saving as an image file within path
img.save(path+FILENAME + '.png')
print("Done :)")