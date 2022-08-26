from inserir import Inserir
from webscrapingF1 import WebscrapingF1


class Main:

    if __name__ == '__main__':

        inserir = Inserir("World_Drivers'_Championship_standings", 'pilotos')
        
        temporadas = ['2005', '2006', '2007', '2008']

        id_pilotos = inserir.get_busca_id()

        nome_dados= inserir.get_nome_dados()

        webscraping = WebscrapingF1()

        
        webscraping.webscrapingF1(temporadas, nome_dados, id_pilotos)