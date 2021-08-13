from selenium import webdriver

driver = webdriver.Chrome()



url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

driver.get(url)

for a_quote in driver.find_elements_by_class_name('quote'):
    print(a_quote.text)