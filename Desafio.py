from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])


website = 'https://www.starz.com/ar/es/movies'
path = 'C:\driver\chromedriver'
driver = webdriver.Chrome(path,chrome_options=options)

driver.get(website)
see_all_movies= driver.find_element_by_css_selector('css=starz-dynamic-container:nth-child(2) .view-all > .text-uppercase')
    
see_all_movies.click()





