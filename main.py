from pilotos.regulamentos_diferentes import RegulamentosDiferentes
from webscraping.criacao_diretorios import Diretorio
from pilotos.dist_e_plots import Dist_e_plots
from pilotos.dataframe_invertido import DataFrameInvertido
from webscraping.webscrapingF1 import WebscrapingF1

class Main:

    if __name__ == '__main__':
        
        temporadas = ['1981','1983','1987','1988','1990'
                    ,'1991','2005', '2006', '2007', '2008',
                    '2010', '2011', '2012', '2013','2018', 
                    '2019', '2020', '2021']

        dataframe = DataFrameInvertido()

        regulamentos_diferentes = RegulamentosDiferentes()

        diretorio = Diretorio()

        webscraping = WebscrapingF1()

        dist_plots = Dist_e_plots()
        
        #criando diretórios para guardar os dataframes conseguidos com o webscraping
        diretorio.criar_diretorio_dataframe('pilotos')
        diretorio.criar_diretorio_dataframe('equipes')
        diretorio.criar_diretorio_dataframe('temporadas')


        for temporada in temporadas:

            #criando pasta da temporada
            diretorio.criar_diretorio_temporada(temporada)
            #criando pasta dos pilotos 
            diretorio.criar_diretorio_pilotos(temporada)
            #criando pasta dos equipes
            diretorio.criar_diretorio_equipes(temporada)

            dataframe.excluindo_ultimas_linhas_e_modificando(temporada)

            dist_plots.novo_dataframe_e_criando_diretorios(temporada)

            dist_plots.dataframe_distribuicoes(temporada)

            regulamentos_diferentes.regulamento_2022(temporada)

            regulamentos_diferentes.pole_e_volta(temporada)

            regulamentos_diferentes.menos_pontos(temporada)

            dist_plots.grafico_pizza(temporada)




        
