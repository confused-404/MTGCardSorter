import camera
import identifier
import scryfall_loader

def main():
    test_card = "Lorien Revealed".lower()
    
    try:
        identifier.getCardName("imgs/" + test_card + ".jpg")
    except:
        scryfall_loader.save_image(test_card, "large")
        
    try:
        identifier.getCardName("imgs/" + test_card + ".jpg")
    except:
        print("ERROR ANALYZING CARD")

if __name__ == '__main__':
    main()