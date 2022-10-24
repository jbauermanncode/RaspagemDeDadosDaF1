from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

from webscraping.criacao_diretorios import Diretorio


class WebscrapingF1:

    diretorio = Diretorio()

    def webscraping_pilotos(self, temporada):

        url = f'https://en.wikipedia.org/wiki/{temporada}_Formula_One_World_Championship'

        response = urlopen(url)
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('span', id = "World_Drivers'_Championship_standings").find_next('table')
        data_frame = pd.read_html( str(table) )[1]

        # guardar um arquivo csv em um diretório
            
        return data_frame


    def webscraping_equipes(self, temporadas):

        for temporada in temporadas:

            url = f'https://en.wikipedia.org/wiki/{temporada}_Formula_One_World_Championship'

            response = urlopen(url)
            html = response.read()

            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('span', id = "World_Drivers'_Championship_standings").find_next('table')
            data_frame = pd.read_html( str(table) )[1]

            # guardar um arquivo csv em um diretório
            data_frame.to_csv(f'./equipes/resultado_equipes_temporada_{temporada}.csv', index=False, encoding='utf-8')
            print(temporada)