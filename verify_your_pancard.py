from PIL import Image
import pytesseract
from selenium import webdriver 
import time
  
driver = webdriver.Firefox() 
driver.get("https://www1.incometaxindiaefiling.gov.in/e-FilingGS/Services/VerifyYourPanDeatils.html?lang=eng")

flag=0

while(1):
	if(flag):
		driver.get("https://www1.incometaxindiaefiling.gov.in/e-FilingGS/Services/VerifyYourPanDeatils.html")
	flag=1
	element = driver.find_element_by_class_name("captchaImgBox") 

	element.screenshot('foo.png') 

	def ocr_core(filename):
	    text = pytesseract.image_to_string(Image.open(filename)) 
	    return text

	pan="DETPS5094J"
	name="RAJESH SHARMA"
	dob="12/07/1969"
	status=1
	captcha=ocr_core('foo.png')

	element1 = driver.find_element_by_id("VerifyYourPanGSAuthentication_pan") 
	element2 = driver.find_element_by_id("VerifyYourPanGSAuthentication_fullName") 
	element3 = driver.find_element_by_id("dateField")
	element4 = driver.find_element_by_id("VerifyYourPanGSAuthentication_status")
	element5 = driver.find_element_by_id("VerifyYourPanGSAuthentication_captchaCode")
	element6 = driver.find_element_by_id("submitbtn")  

	element1.send_keys(pan)
	element2.send_keys(name)
	element3.send_keys(dob)
	element4.send_keys(status);
	element5.send_keys(captcha)
	element6.submit()

	time.sleep(1.5)
	error=0
	try:
		error = driver.find_element_by_class_name("error")
	except:
		print("verified")
		break
	else:
		if(error.get_attribute('innerHTML')!=" Invalid Code. Please enter the code as appearing in the Image." and error.get_attribute('innerHTML')!="\n Invalid Code. Please enter the code as appearing in the Image." and error.get_attribute('innerHTML')!="\n Please enter the code as appearing in the Image." and error.get_attribute('innerHTML')!=" Please enter the code as appearing in the Image."):
			print(error.get_attribute('innerHTML'))
			break