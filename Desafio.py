from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])


website = 'https://www.starz.com/ar/es/movies'
path = 'C:\driver\chromedriver'
driver = webdriver.Chrome(path,chrome_options=options)

driver.get(website)

try:
    element = WebDriverWait (driver,50).until(EC.presence_of_element_located((By.ID, "subview-container")))
    xpath='//*[@id="subview-container"]/starz-movies/div/starz-block-page-render/div/starz-dynamic-container[2]/div/div/div/starz-std-slider/div/div[1]/a/div'

    xpath2="//section[@id='subview-container']/starz-movies/div/starz-block-page-render/div/starz-dynamic-container[2]/div/div/div/starz-std-slider/div/div/a/div"
    cssSlect="//section[@id='subview-container']/starz-movies/div/starz-block-page-render/div/starz-dynamic-container[2]/div/div/div/starz-std-slider/div/div/a/div"

    see_all_movies= driver.find_element_by_xpath(xpath)
    
    see_all_movies.click()
finally:
    driver.quit()





