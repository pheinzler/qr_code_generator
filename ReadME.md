# ReadME

This Python script allows you to generate a qr_code with a given string argument.

## Usage

To use this script you need to specify the requested QR_Code Data in config.py "DATA".
With the "FILENAME" in config.py you can specify the name of the save QR_Code image.
You DO NOT need to speficy the file type. The filetype will be added within the script.
If there is no filename given, a random filename will be created.

## QR_Codes

The generated QR_Codes will be stored in /qr_codes/date.

## Requirements

You may need to install pyyaml and qrcode (pip install)
