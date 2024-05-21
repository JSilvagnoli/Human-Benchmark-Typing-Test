from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import io
import imageFromText
import typeText
import pyautogui
import re

def OpenPage():
    # Initialize the WebDriver (Chrome in this case)
    driver = webdriver.Chrome()

    # Navigate to the webpage
    driver.get('https://humanbenchmark.com/tests/typing')
    
    return driver
    
def Screenshot(driver):

    # Find the element by its class name
    element = driver.find_element(By.CSS_SELECTOR, '.letters.notranslate')

    # Get the element's location and size
    location = element.location
    size = element.size

    # Take a full-page screenshot
    png = driver.get_screenshot_as_png()

    # Open the image with PIL
    image = Image.open(io.BytesIO(png))

    # Calculate the bounds
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    # Crop the image to the bounds of the element
    image = image.crop((left, top, right, bottom))

    # Save the image
    image.save(r'C:\Users\silva\Desktop\Resume Projects\Human Benchmark Test Typing Python Project\text_screenshot.png')
        
    text = imageFromText.extractTextFromImage()
        
    if text.startswith('['):
        text = text[1:]
            
    # Remove line breaks
    text = text.replace('\n', ' ')

    # Print the extracted text
    print("Extracted Text:", text)

    # Type all characters except the last one or two
    typeText(text)

    
def typeText(text):
    # Type the text using pyautogui
    pyautogui.write(text, interval = 0)