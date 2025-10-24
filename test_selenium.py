from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


service = Service("C:\\Users\\D00509821\\PATH\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://isitchristmas.com")

answer = driver.find_element(By.ID, "answer")

print("Page title: ", driver.title)
print("Answer text: ", answer.text)
driver.quit()