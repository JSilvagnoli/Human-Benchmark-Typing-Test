import pytesseract
from PIL import Image
import typeText

def extractTextFromImage():
    # Path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load an image from file
    image = Image.open('text_screenshot.png')

    # use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    
    print(text)
    return text