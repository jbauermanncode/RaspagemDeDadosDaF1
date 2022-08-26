from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

class WebscrapingF1:

    def webscrapingF1(self, temporadas, nome_dados,  busca_id):

        for temporada in temporadas:

            url = f'https://en.wikipedia.org/wiki/{temporada}_Formula_One_World_Championship'

            response = urlopen(url)
            html = response.read()

            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('span', id = busca_id).find_next('table')
            data_frame = pd.read_html( str(table) )[0]

            # criar e guardar um arquivo csv em um diretório
            data_frame.to_csv(f'./dados_{nome_dados}/resultado_{nome_dados}_temporada_{temporada}.csv', index=False, encoding='utf-8')
            print(temporada)



