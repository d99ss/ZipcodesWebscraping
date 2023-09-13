# Project description :spider_web:
<p align="center">The Goal of this project was to get all of the data available including zip codes, neighborhoods, latitudes, longitudes, and so forth so on of the City of São Paulo from the <a href="https://cepbrasil.org/">🔗 Cep Brasil</a>, and export it to an Excel file. There are a lot of websites containing this data but I chose this one because I deemed it more reliable, Please be aware It is not an official database, the real database is provided by the Correios with a price of **($Thanks Correios$)** since it is public information I chose not to pay it and do the old and good web scrapping, so therefore it should have zip codes that no longer work or new ones added to the official base that are not in this one, also bear in mind that values such lat and lon are not accurately right.</p>

## Library :books:
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=selenium" />
    :panda_face:
  </a>
</p>

<p align="center">I used Selenium and Pandas, Selenium to automate the page, and Pandas to read the Excel files containing the ceps and to export to a new Excel file the data scrapped.</p>

## Website structure :building_construction:	

<p align="center">
  Be aware the structure can change over time.
  At the time of this writing here is the current structure:
  You have the parents' hyperlinks with the names of the neighborhoods and 
  Inside each hyperlink, there are the neighborhoods' streets or the children's.
</p>
  
    - Aclimação
        - CEP 01526-000 - Rua Bueno de Andrade ...
    - Água Branca
        - CEP 05001-000 - Avenida Francisco Matarazzo ...
    - Água fria
        - CEP 02330-970 - Avenida Nova Cantareira, 942 ...
      
  <p align="center">
  I realized halfway through the project that getting all the links was way better than iterating between the parent and children back and forth.
  This step was not only efficient but prone to errors.
  
  - *Aclimação -> CEP 01526-000* 
  - *Aclimação -> Next Zip code* 
  
  The links basically stay the same only changing a few parts:
  - https://cepbrasil.org/sao-paulo/sao-paulo/agua-branca
     - https://cepbrasil.org/sao-paulo/sao-paulo/agua-branca/05001000
  - https://cepbrasil.org/sao-paulo/sao-paulo/aclimacao
     - https://cepbrasil.org/sao-paulo/sao-paulo/aclimacao/01526000
      
  First I got all the hyperlinks 
  containing the neighborhoods' streets such as * https://cepbrasil.org/sao-paulo/sao-paulo/agua-fria/02330970 *, and exported it to an Excel file.
  Second I read the URLs from the Excel file and used them as links to get to the browser. 
  Using this approach of entering each page that you want to webscrape you avoid issues such as TimeOutException or Netwoork error. 
  The code can easily be modified to get Brazil's other cities/neighborhoods.<br>
  You can find the data scrapped on my <a href="https://www.kaggle.com/datasets/mrlogicalwolverine/sp-data" target="_blank">**~~Kaggle~~**</a>.
</p>


