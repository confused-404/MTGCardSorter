### ATTEMPT WITH OCR ###

import pytesseract
import numpy as np
from PIL import Image
import re
import os

# returns name, set, collector number of card from image containing card using OCR
# in the form of a dictionary
def getCardName(img_path):
    setcodepattern = r"(?<=\s)[A-Z]{2,}[A-Z1-9]{1}(?=\s*[!-/:-@[-`{-~+_©]|\s*\+\s*)|(?<=\s)[M]\d+(?=\s+)|(?<=\s)[A-Z]{3}(?=\s+[+])"
    collectorpattern = r"(?<=[URCMLurcml¢€]\s)\d+(?=\s+)|(?<=\s)\d+(?=\s+[€URCMLurcml¢]\s+[a-zA-Z])|(?<=\s)\d{2,}(?=\/\d+\s+[€URCMLurcml¢])|(?<=\s)\d+(?=\s[!@#$%^&*_+]+)"
    
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    img = Image.open(img_path)
    img = img.crop((0, img.height/2, img.width / 2, img.height)).convert("L")
    
    if not (os.path.isfile("imgs/cropped/" + img_path.split("/")[-1].split(".")[0] + "_cropped.jpg")):
            img.save("imgs/cropped/" + img_path.split("/")[-1].split(".")[0] + "_cropped.jpg")
    
    
    arr = np.array(img)
    
    raw = pytesseract.image_to_string(arr)
    
    # print("\n\n" + raw + "\n\n")
    
    setcode = ""
    collector = -1
    
    try:
        setcode = re.findall(pattern=setcodepattern, string=raw)[0]
    except:
        print("Set Code FAILURE")
        
    try:
        collector = re.findall(pattern=collectorpattern, string=raw)[0]
        # print("Collector Number: " + collector)
    except:
        print("Collector Number FAILURE")
    
    if (collector != -1 and setcode != ""):
        print(setcode + " " + str(collector))
    else:
        print(raw)

    