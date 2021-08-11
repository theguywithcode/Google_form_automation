
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

flink = input("Please Enter Link to the Google Form")
driver = webdriver.Chrome(
	'C:/Users/mehul/Downloads/chromedriver_win32/chromedriver.exe')


driver.get(flink)


time.sleep(1)


datas = [
	['thomas','pandu' ],
    ['petter','patter'],
    
]


for data in datas:
	count = 0
	textboxes = driver.find_elements_by_class_name(
		"quantumWizTextinputPaperinputInput")

	textareaboxes = driver.find_elements_by_class_name(
		"quantumWizTextinputPapertextareaInput")


	for value in textboxes:
		value.send_keys(data[count])

		count += 1


	for value in textareaboxes:

		value.send_keys(data[count])

		count += 1


	submit = driver.find_element_by_xpath(
		'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
	submit.click()


	another_response = driver.find_element_by_xpath(
		'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
	another_response.click()


driver.close()
