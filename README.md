# Human-Benchmark-Typing-Test

## Overview
This application breaks the Human Benchmark Typing Test by using Python, Selenium, Tesseract, and PyAutoGUI

## Features
- Reache upwards of 15,000 words typed per minute placing you in the 99.9% percentile on the Human Benchmark Typing Test

## Technologies Used
- Python
- Selenium
- Tesseract
- PyAutoGUI

## Installation
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/JSilvagnoli/Human-Benchmark-Typing-Test.git
2. Navigate to the project directory
   ```sh
   cd Human-Benchmark-Typing-Test
3. Go to:
  ```
  https://developer.chrome.com/docs/chromedriver/downloads
   ```

4. Click on "the Chrome for Testing availability dashboard".
This will take you to download the most up to date ChromeDriver.
Ensure that you download the ChromeDriver for your version of Chrome.

5. Install Selenium using pip
   ```
   pip install selenium
   ```
6. Go To:
  ```
  https://github.com/tesseract-ocr/tesseract
   ```
7. Follow the instructions on the GitHub repository to download Tesseract.
8. Install PyTesseract using pip:
   ```
  pip install pytesseract
   ```

10. Install PyAutoGUI using pip:
   ```
   pip install pyautogui
   ```

## Usage
1. Run typingTestAutomation.py

## Contributing
1. Fork the repository.
2. Create a new branch: git checkout -b my-feature-branch
3. Make your changes and commit them: git commit -m 'Add some feature'
4. Push to the branch: git push origin my-feature-branch
5. Submit a pull request.

## Disclaimer
Please note that while this application aims to break the Human Benchmark Typing Test by automating typing, there may be instances where the OCR (Optical Character Recognition) process using Tesseract does not accurately extract characters from the test prompt. This can result in unexpected behavior, such as incomplete typing or lower than expected words per minute (WPM) scores.

Additionally, the accuracy and performance of the typing test may vary depending on the complexity and formatting of the prompt. Sometimes, the program may not finish typing, and the WPM score may be significantly lower than anticipated.

It's important to understand that these limitations are inherent to the OCR process and the nature of automating typing tests. While efforts have been made to improve consistency, there may still be occasional discrepancies.

We appreciate your understanding and patience as we continue to refine and enhance the functionality of this application. If you encounter any issues or have suggestions for improvement, please feel free to report them via GitHub issues.
