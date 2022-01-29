Web Scrapping desarrollado en Python con las librerias Selenium y Pandas, al sitio www.starz.com/ar

- Se mantuvieron las referecias a Movies por no modificar todo el codigo, lo ideal seria refactorizar ambos y hacer todo en uno donde por parametros se pasen los distintos xpath y quedaria un codigo mucho mas limpio, unificado y reutilizable
- Se debe correr cada script independiente para series y pelicuas y genera un archivos .csv respectivo a cada script
- Ambos scripts cargan desde el home la pagina y navegan hasta la secccion completa de peliculas/series
- Se extraen los links de cada pelicula/serie y luego con cada uno se accede a los correspondientes titulos.
- Para las sinopsis agregue un try, except, que primero intente hacer click en "mas.." para obtener la sinopsis completa! en caso de no estar dicho "boton" toma el valor de la sinopsis tal cual se ve en pantalla.
