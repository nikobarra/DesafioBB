
from sys import meta_path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

link_movie_array=[]

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])#con estas options evito que de error usb y bluetooth

website = 'https://www.starz.com/ar/es/'
path = 'C:\driver\chromedriver'
driver = webdriver.Chrome(path,chrome_options=options)
driver.implicitly_wait(10) #un tipo de timer para que de tiempo de carga a la pagina y encuentre los elementos clickeables ya renderizados en el dom
driver.get(website)

xpath='//*[@id="view-container"]/starz-header/header/div/div/div[4]/button/span[1]'#path del menu hamburguesa 
xpath2='//*[@id="application-wrapper"]/starz-sidebar/div/div/ul/li[3]/a'#path click peliculas
xpath3= '//*[@id="subview-container"]/starz-movies/div/starz-block-page-render/div/starz-dynamic-container[2]/div/div/div/starz-std-slider/div/div[1]/a/div' #path ver todas

def click_movies(xpath):
    see_all_movies= driver.find_element_by_xpath(xpath) 
    see_all_movies.click()


click_movies(xpath)
click_movies(xpath2)
click_movies(xpath3)
time.sleep(2)

movies = driver.find_elements_by_xpath("//section//a[@href]") #obtengo los elementos href de cada pelicula del catalogo

for movie in movies:
    link_movie_array.append(movie.get_attribute("href")) #recorro el array obtenido con los elementos href y extraigo solo los links
    #print (movie.get_attribute("href"))

link_movie_array = list(set(link_movie_array))#elimino los links duplicados del array


for pelicula in link_movie_array: #recorro cada link obteniendo toda la info necesaria
    driver.get(pelicula)
    name_movie = driver.find_element_by_xpath('//*[@id="moviesDetailsH1"]')
    meta_movie = driver.find_elements_by_xpath('//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul')

    path_sinop = '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/button/span'
    try:#si la sinopsis tiene el clickeable Mas intento clickearlo, si no lo tiene uso el parrafo tal cual esta en la pagina
        click_movies(path_sinop)
        sinop_movie = driver.find_element_by_xpath('//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/p[1]')
    except:
        sinop_movie = driver.find_element_by_xpath('//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/p')

    print (name_movie.text)
    print (sinop_movie.text)

    for meta in meta_movie:
        print(meta.text)
    
    

