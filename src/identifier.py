### ATTEMPT WITH OCR ###

import pytesseract
import numpy as np
from PIL import Image, ImageFilter
import re
import os

# returns name, set, collector number of card from image containing card using OCR
# in the form of a dictionary
def getCardName(img_path):
    setcodepattern = r"(?<=\s)[A-Z]{2,}[A-Z1-9]{1}(?=\s*[!-/:-@[-`{-~+_©«]|\s*\+\s*)|(?<=\s)[M]\d+(?=\s+|\+)|(?<=\s)[A-Z]{3}(?=\s+[+])"
    collectorpattern = r"\d+(?=\/\d+\s[UCMRLucmrl])|\d+(?=\s+[URCMLucmrl])|(?<=[UCMRLucmrl]\s)\d+(?=\s+[A-Za-z]{3,})|(?<=\s)\d+(?=\s+[!@#$%^&*()]\s+[A-Z]{3,})"
    
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    
    raw_img = Image.open(img_path)
    input_name = img_path.split("/")[-1].split(".")[0]
    
    setcode_img = raw_img.crop((raw_img.width / 20, raw_img.height/1.05, raw_img.width / 7, raw_img.height / 1.02))
    setcode_img.save("imgs/cropped/setcode/" + input_name + ".jpg")
    
    set_code = pytesseract.image_to_string(setcode_img)
    
    set_code = re.sub(string=set_code, pattern="\W", repl="")
    
    print(set_code)

    