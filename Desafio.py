from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])#con estas options evito que de error usb y bluetooth

website = 'https://www.starz.com/ar/es/'
path = 'C:\driver\chromedriver'
driver = webdriver.Chrome(path,chrome_options=options)
driver.implicitly_wait(20) #un tipo de timer para que de tiempo de carga a la pagina y encuentre los elementos clickeables ya renderizados en el dom
driver.get(website)

xpath='//*[@id="application-wrapper"]/starz-sidebar/div/div/ul/li[3]/a'#path click peliculas

xpath2='//*[@id="view-container"]/starz-header/header/div/div/div[4]/button/span[1]'#path del menu hamburguesa 

xpath3= '//*[@id="subview-container"]/starz-movies/div/starz-block-page-render/div/starz-dynamic-container[2]/div/div/div/starz-std-slider/div/div[1]/a/div' #path ver todas

def click_movies(xpath):
    see_all_movies= driver.find_element_by_xpath(xpath) 
    see_all_movies.click()


click_movies(xpath2)
click_movies(xpath)
click_movies(xpath3)


