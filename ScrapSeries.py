#Se mantuvieron las referecias a Movies por no modificar todo el codigo, lo ideal seria refactorizar ambos y hacer todo en uno donde por paramtros se pasen los distintos xpath y quedaria un codigo mucho mas limpio, unificado y reutilizable



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

link_movie_array=[]

full_movie_array = []

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])#con estas options evito que de error usb y bluetooth

website = 'https://www.starz.com/ar/es/'
path = 'C:\driver\chromedriver'
driver = webdriver.Chrome(path,chrome_options=options)
driver.implicitly_wait(10) #un tipo de timer para que de tiempo de carga a la pagina y encuentre los elementos clickeables ya renderizados en el dom
driver.get(website)

xpath='//*[@id="view-container"]/starz-header/header/div/div/div[4]/button/span[1]'#path del menu hamburguesa 
xpath2='//*[@id="application-wrapper"]/starz-sidebar/div/div/ul/li[2]/a'#path click series
xpath3= '//*[@id="subview-container"]/starz-series/div/starz-block-page-render/div/starz-dynamic-container[1]/div/div/div/starz-std-slider/div/div[1]/a/div' #path ver todas series


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
    driver.get(pelicula)#la variable pelicula contiene el link a cada una
    name_movie = driver.find_element_by_xpath('//*[@id="seriesDetailsH1"]')
    meta_movie = driver.find_elements_by_xpath('//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li')

    path_sinop = '//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/div[2]/button/span'
    try:#si la sinopsis tiene el clickeable Mas intento clickearlo, si no lo tiene uso el parrafo tal cual esta en la pagina
        click_movies(path_sinop)
        sinop_movie = driver.find_element_by_xpath('//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/div[2]/p[1]')
        
    except:
        sinop_movie = driver.find_element_by_xpath('//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/div[2]/p')


    full_movie_array.append (name_movie.text)
    full_movie_array.append (sinop_movie.text)
    full_movie_array.append (pelicula)
    
    meta_data_movie=[]
    for meta in meta_movie:
        print(meta.text)
        meta_data_movie.append(meta.text)
    
    full_movie_array.append(meta_data_movie)
    

driver.close()

df = pd.DataFrame({'full_movie_array':full_movie_array})
df.to_csv('./Desafio/MetaDataSeries.csv', index=False)    




