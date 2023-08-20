# Project description
<p align="center">The Goal of this project was to get all of the data available including zip codes, neighborhoods, latitudes, longitudes so forth so on of the City of São Paulo from the <a href="https://cepbrasil.org/">🔗 Cep Brasil</a>, and export it to an Excel file.</p>

## Library
<p align="center">I used Selenium and Pandas, Selenium to automate the page, and Pandas to read the Excel files containing the ceps and to export to a new Excel file the data scrapped.</p>

## Website structure

<p align="center">
  Be aware the structure can change over time.
  You have the hyperlinks with the names of the neighborhoods:
  
    - Aclimação
      - CEP 01526-000 - Rua Bueno de Andrade 
    - Água Branca
    - Água fria
    
  Inside each hyperlink, there are the neighborhoods' streets
    - Aclimação
    ...
    - Água Branca
    - CEP 05001-000 - Avenida Francisco Matarazzo ...
    - Água fria
    - CEP 02330-970 - Avenida Nova Cantareira, 942 ...
  
  Since I want it to get all the neighborhoods instead of looping it through the neighborhood names back and forth, first I got all the hyperlinks 
  containing the neighborhoods' streets such as * https://cepbrasil.org/sao-paulo/sao-paulo/agua-fria/02330970 *, and export it to an Excel file.
  Second I read the URLs from the Excel file and used them as links to get to the browser. 
  Using this approach of entering each page that you want to webscrape you avoid issues such as TimeOutException or Netwoork error. 
  The code can easily be modified to get Brazil's other cities/neighborhoods.
</p>

