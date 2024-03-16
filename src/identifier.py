### ATTEMPT WITH OCR ###

import pytesseract
import numpy as np
from PIL import Image, ImageFilter
import re
import os

# returns name, set, collector number of card from image containing card using OCR
# in the form of a dictionary
def getCardName(img_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    
    raw_img = Image.open(img_path)
    input_name = img_path.split("/")[-1].split(".")[0]
    
    name_img = raw_img.crop((raw_img.width/15, raw_img.height/20, raw_img.width/1.3, raw_img.height / 10))
    # name_img = name_img.resize((name_img.width*10, name_img.height*10), resample=Image.BOX)
    # name_img = name_img.filter(ImageFilter.BLUR)
    name_img.save("imgs/cropped/name/" + input_name + ".jpg")
    
    card_name = pytesseract.image_to_string(name_img)
    card_name = re.sub(string=card_name, pattern=r"[^\w\s]", repl="")
    card_name = card_name.strip()
    
    return card_name
    
def getSetCode(img_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    
    raw_img = Image.open(img_path)
    input_name = img_path.split("/")[-1].split(".")[0]
    
    setcode_img = raw_img.crop((raw_img.width / 20, raw_img.height/1.05, raw_img.width / 8.25, raw_img.height / 1.02))
    setcode_img = setcode_img.resize((setcode_img.width*10, setcode_img.height*10), resample=Image.BOX)
    setcode_img = setcode_img.filter(ImageFilter.BLUR)
    setcode_img.save("imgs/cropped/setcode/" + input_name + ".jpg")
    
    set_code = pytesseract.image_to_string(setcode_img)
    set_code = re.sub(string=set_code, pattern=r"[^[A-Z]]", repl="")
    set_code = set_code.strip()
    
    return set_code

    