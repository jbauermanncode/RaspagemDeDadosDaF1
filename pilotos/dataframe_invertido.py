from webscraping.webscrapingF1 import WebscrapingF1
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import dataframe_image as dfi
from pathlib import Path

class DataFrameInvertido:

    dados = WebscrapingF1()

    def excluindo_ultimas_linhas_e_modificando(self, temporada):

        dataframe = self.dados.webscraping_pilotos(temporada)

        #excluir linhas
        if ((temporada == '1981') or (temporada == '1983') or (temporada == '1987') 
                or (temporada ==  '1988') or (temporada == '1990') or (temporada == '2019')):
            exclui = 1
            
        elif ((temporada == '1991') or (temporada == '2005') or (temporada == '2006') 
                or (temporada == '2007') or (temporada == '2008') or (temporada == '2010') 
                or (temporada == '2011') or (temporada == '2012') or (temporada == '2018') 
                or (temporada == '2020') or (temporada == '2021')): 
            exclui = 2
            if (temporada == '2007'):
                dataframe.drop(columns=['Unnamed: 20'], inplace=True)
            elif (temporada == '2011') or (temporada == '2012') or (temporada == '2020'):
                lista = []
                if (temporada == '2011'):
                    numeros = list(range (22,30))
                elif (temporada == '2012'):
                    numeros = list(range (23,25))
                elif (temporada == '2020'):
                    numeros = list(range (20,30))
                for i in numeros:
                    unnamed = f'Unnamed: {i}'
                    lista.append(unnamed)
                dataframe.drop(columns=lista, inplace=True)
        elif (temporada == '2013'): 
            exclui = 3
        dataframe.drop(dataframe.tail(exclui).index, inplace=True)
        
        #modificar os dados NaN por -
        dataframe.fillna(value = '-', inplace = True)

        dataframe.to_csv(f'./temporadas/temporada-{temporada}/pilotos/resultado-pilotos-original-{temporada}.csv', index=True, encoding='utf-8')
        dfi.export(dataframe,f'./temporadas/temporada-{temporada}/pilotos/resultado-pilotos-original-{temporada}.png', table_conversion='matplotlib')

        return dataframe

    ## apagando coluna e definindo o index e invertendo o dataframe
    def invertendo_dataframe(self, temporada):

        dataframe = self.excluindo_ultimas_linhas_e_modificando(temporada)
        
        # apagando coluna 'Posição'
        if ((temporada == '1981') or (temporada == '1983') or (temporada == '1987') or (temporada == '1988')):
            posicao = 'Pos'
        elif ((temporada == '1990') or (temporada == '2005') or (temporada == '2006') 
                or (temporada == '2007') or (temporada == '2008') or (temporada == '2010') 
                or (temporada == '2011') or (temporada == '2012') or (temporada == '2013') 
                or (temporada == '2018') or (temporada == '2019') or (temporada == '2020') 
                or (temporada == '2021')):
            posicao = 'Pos.'
        elif (temporada == '1991'):
            posicao = '.mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}Pos.'

        dataframe_invertido = dataframe.drop(columns=[posicao])
        # definindo 'Driver' como index
        
        dataframe_invertido = dataframe_invertido.set_index('Driver')
        # invertendo colunas e linhas do DataFrame
        dataframe_invertido = dataframe_invertido.T
        
        # apagando a linha 'Pontos
        if ((temporada == '1981') or (temporada == '1991') or (temporada == '2005') 
                or (temporada == '2006') or (temporada == '2007') or (temporada == '2008') 
                or (temporada == '2010') or (temporada == '2011') or (temporada == '2012') 
                or (temporada == '2013') or (temporada == '2018') or (temporada == '2019') 
                or (temporada == '2020') or (temporada == '2021')):

            pontos = 'Points'
        elif (temporada == '1983'):
            pontos = 'Pts'
        elif (temporada == '1987'):
            pontos = 'Points[1]'
        elif (temporada == '1988') or (temporada == '1990'):
            pontos = 'Points[a]'
            
        dataframe_invertido = dataframe_invertido.drop(pontos)

        return dataframe_invertido

