from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get('https://chromedino.com/')

while True:
    ActionChains(driver).send_keys(Keys.ARROW_UP).perform()