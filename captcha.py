from PIL import Image
import pytesseract
from selenium import webdriver 

driver = webdriver.Chrome("C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe") 

 
driver.get("https://www1.incometaxindiaefiling.gov.in/e-FilingGS/Services/VerifyYourPanDeatils.html?lang=eng") 
  
element = driver.find_element_by_class_name("captchaImgBox") 

element.screenshot('captcha.png') 

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core('captcha.png'))