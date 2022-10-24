import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
import numpy as np
import seaborn as sns
from pilotos.modificandoPontos import ModificandoPontos
from webscraping.criacao_diretorios import Diretorio
from pilotos.dataframe_invertido import DataFrameInvertido

class Dist_e_plots:

    diretorio = Diretorio()

    dados_piloto = DataFrameInvertido()

    modificandoPontos = ModificandoPontos()

    def organizando_posicoes(self, temporada):

        ajustar_posicoes = self.modificandoPontos.ajuste_posicoes(temporada)
        data_frame = self.dados_piloto.invertendo_dataframe(temporada)
        
        # criar uma lista para criar um DataFrame com as posiçoes uniformizadas
        lista_ajustar_posicoes = []
        for i in data_frame.columns:
            piloto = data_frame[i].map(ajustar_posicoes)
            lista_ajustar_posicoes.append(piloto)
        return lista_ajustar_posicoes
    
    def novo_dataframe_e_criando_diretorios(self, temporada):
        ajustar_posicoes = self.organizando_posicoes(temporada)
        # criar DataFrame
        data_frame = pd.DataFrame(ajustar_posicoes)
        # inverter linhas e colunas
        data_frame = data_frame.T

        for piloto in data_frame.columns:
            #criando diretório dos pilotos
            piloto = piloto.replace(' ','')
            self.diretorio.criar_diretorio_para_cada_piloto(temporada, piloto)
        
        return data_frame
    
    def dataframe_distribuicoes(self, temporada):
        
        data_frame = self.novo_dataframe_e_criando_diretorios(temporada)
        for piloto in data_frame.columns:
            # distribuição de frequência
            frequencia = data_frame[piloto].value_counts()
            # distribuição de percentual
            percentual = (data_frame[piloto].value_counts(normalize=True) * 100).round(2)

            # criar DataFrame
            dist_freq = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})
            dist_freq = dist_freq.rename_axis('Posição', axis='index')
            # guardar DataFrame
            piloto = piloto.replace(" ", "")
            dist_freq.to_csv(f'./temporadas/temporada-{temporada}/pilotos/{piloto}/dist-freq-{piloto}-{temporada}.csv', index=True, encoding='utf-8')
            dfi.export(dist_freq, f'./temporadas/temporada-{temporada}/pilotos/{piloto}/dist-freq-{piloto}-{temporada}.png', table_conversion='matplotlib')


    def grafico_frequencias(self, temporada):
        
        data_frame = self.novo_dataframe_e_criando_diretorios(temporada)
        # grafico de barras horizontais
        for i,piloto in enumerate(data_frame.columns):
            
            plt.figure(i) # usa_se esse comando para um grafico não plotar sobre o outro

            # distribuição de frequencia
            frequencia = data_frame[piloto].value_counts()
            # plotando o grafico
            ax = frequencia.plot(kind='barh', linestyle='dashed')
            # dimensões do grafico
            ax.figure.set_size_inches(12,6)
            # titulo e fonte do titulo
            ax.set_title(f'Distribuiçaõ de Frequências das Posições de {piloto}', fontsize = 16)
            # titulo eixo X
            ax.set_xlabel('Frequência', fontsize=14)
            # titulo eixo Y
            ax.set_ylabel('Posições', fontsize=14)
            # guardando imagem do grafico
            piloto = piloto.replace(" ", "")
            ax.get_figure().savefig(f'./temporadas/temporada-{temporada}/pilotos/{piloto}/frequencia-plot-{piloto}-{temporada}.png')

    def grafico_porcentagens(self, temporada):

        data_frame = self.novo_dataframe_e_criando_diretorios(temporada)
        # grafico de barras vertical
        for i,piloto in enumerate(data_frame.columns):
            plt.figure(i)
            percentual = (data_frame[piloto].value_counts(normalize=True) * 100).round(2)

            bx = percentual.plot.bar(width=1, alpha=0.2,figsize=(12,6))
            bx.figure.set_size_inches(12,6)
            bx.set_title(f'Distribuiçaõ de Porcentagem das Posições de {piloto}', fontsize = 16)
            bx.set_xlabel('Posições', fontsize=14)
            bx.set_ylabel('Porcentagem (%)', fontsize=14)
            # guardando imagem do grafico
            piloto = piloto.replace(" ", "")
            bx.get_figure().savefig(f'./temporadas/temporada-{temporada}/pilotos/{piloto}/porcentagem-plot-{piloto}-{temporada}.png')

    def grafico_pizza(self, temporada):

        data_frame = self.novo_dataframe_e_criando_diretorios(temporada)
        # grafico de pizza
        for i,piloto in enumerate(data_frame.columns):
            plt.figure(i)

            piloto = piloto.replace(" ", "")

            dist_freq = pd.read_csv(f'./temporadas/temporada-{temporada}/pilotos/{piloto}/dist-freq-{piloto}-{temporada}.csv')

            colors = sns.color_palette('pastel')
            legenda = dist_freq['Posição']
            percentual = dist_freq['Porcentagem (%)']

            fig,ax = plt.subplots(figsize=(10,7), subplot_kw=dict(aspect='equal'))

            ax.pie(percentual, autopct='%.0f%%', pctdistance=1.15, colors=colors)

            ax.legend(legenda, title='Posições', loc='center left', bbox_to_anchor=(1.25,0,0.5,1))

            ax.set_title(f'Grafico de Pizza de {piloto}')

            ax.get_figure().savefig(f'./temporadas/temporada-{temporada}/pilotos/{piloto}/pie-plot-{piloto}-{temporada}.png')




