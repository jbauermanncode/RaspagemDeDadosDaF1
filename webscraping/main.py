from inserir import Inserir
from webscrapingF1 import WebscrapingF1


class Main:

    if __name__ == '__main__':

        campeonato_pilotos = "World_Drivers'_Championship_standings"

        campeonato_equipes = "World_Drivers'_Championship_standings"

        inserir = Inserir(campeonato_equipes, 'equipes')
        
        temporadas = ['2005', '2006', '2007', '2008']

        busca_id = inserir.get_busca_id()

        nome_dados= inserir.get_nome_dados()

        webscraping = WebscrapingF1()

        
        webscraping.webscrapingF1(temporadas, nome_dados, busca_id)