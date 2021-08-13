from selenium import webdriver
driver = webdriver.Chrome()

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver.get(url)

input('Press ENTER to close the automated browser')
driver.quit()