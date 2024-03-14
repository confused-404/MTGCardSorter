### ATTEMPT WITH OCR ###

import pytesseract
import numpy as np
from PIL import Image
import re

# returns name, set, collector number of card from image containing card using OCR
# in the form of a dictionary
def getCardName(img_path):
    setcodepattern = r"(?<=\s)[A-Z]{3,}(?=\s\+\s)"
    collectorpattern = r"(?<=[U|R|C|M|L]\s)\d+\d+|(?<=\s)\d+(?=/\d+\s+[U|R|C|M|L]\s+[a-zA-Z])"
    
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    arr = np.array(Image.open(img_path))
    
    raw = pytesseract.image_to_string(arr)
    
    collector = re.findall(pattern=collectorpattern, string=raw)[0]
    setcode = re.findall(pattern=setcodepattern, string=raw)[0]
    
    print(setcode + " " + str(collector))

    