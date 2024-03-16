import camera
import identifier
import scryfall_loader
import os

def main():
    
    testing = True
    
    while (testing):
        test_card = input("Enter card name: ").lower()
        
        if not (os.path.isfile("imgs/raw/" + test_card + ".jpg")):
            scryfall_loader.save_image(test_card, "large")
            
        identifier.getCardName("imgs/raw/" + test_card + ".jpg")
    
if __name__ == '__main__':
    main()