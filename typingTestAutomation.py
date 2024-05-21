import webpageOpener
import imageFromText

if __name__ == "__main__":
    driver = None
    try:
        while True:
            if driver is None:
                driver = webpageOpener.OpenPage()
            else:
                driver.refresh()
            webpageOpener.Screenshot(driver)
            choice = input("Press Enter to run the code again, or type 'exit' to quit: ")
            if choice.lower() == 'exit':
                break
    finally:
        if driver is not None:
            driver.quit()

