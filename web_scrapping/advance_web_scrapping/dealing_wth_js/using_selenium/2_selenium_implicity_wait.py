from selenium import webdriver

driver = webdriver.Chrome()

# set an implicity wait
driver.implicitly_wait(10)

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

driver.get(url)

for a_quote in driver.find_elements_by_class_name('quote'):
    print(a_quote.text)

input('Press ENTER to close automated browser')
driver.quit()
