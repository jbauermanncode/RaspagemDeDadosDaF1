import pandas as pd
import dataframe_image as dfi
import matplotlib.pyplot as plt
import seaborn as sns

from dataframe_invertido import DataFrameInvertido
from modificandoPontos import ModificandoPontos


class DistFreq:

    dataframe_invertido = DataFrameInvertido()
    modificandoPontos = ModificandoPontos()

    def novo_dataframe(self, temporada):

        ajustar_posicoes = self.modificandoPontos.ajuste_posicoes(temporada)
        
        novo_dataframe = self.dataframe_invertido.invertendo_dataframe(temporada)

        # criar uma lista para criar um DataFrame com as posiçoes uniformizadas
        lista_ajustar_posicoes = []
        for i in novo_dataframe.columns:
            piloto = novo_dataframe[i].map(ajustar_posicoes)
            lista_ajustar_posicoes.append(piloto)
        # criar DataFrame
        novo_data_frame = pd.DataFrame(lista_ajustar_posicoes)
        # inverter linhas e colunas
        novo_data_frame = novo_data_frame.T
        return novo_data_frame

    #construir DataFrames das distribuições
    def dist_freq(self, temporada):

        novo_dataframe = self.novo_dataframe(temporada)        

        for piloto in novo_dataframe.columns:
            # distribuição de frequência
            frequencia = novo_dataframe[piloto].value_counts()
            # distribuição de percentual
            percentual = (novo_dataframe[piloto].value_counts(normalize=True) * 100).round(2)

            # criar DataFrame
            dist_freq = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})
            dist_freq = dist_freq.rename_axis('Posição', axis='index')
            # guardar DataFrame
            piloto = piloto.replace(" ", "")
            dist_freq.to_csv(f'./temporadas/temporada-{temporada}/pilotos/{piloto}/dist-freq-{piloto}-{temporada}.csv', index=True, encoding='utf-8')
            dfi.export(dist_freq, f'./temporadas/temporada-{temporada}/pilotos/{piloto}/dist-freq-{piloto}-{temporada}.png', table_conversion='matplotlib')

     # grafico de barras horizontais
    def plot_bar(self, temporada):

        novo_dataframe = self.novo_dataframe(temporada) 

        for i,piloto in enumerate(novo_dataframe.columns):
            
            plt.figure(i) # usa_se esse comando para um grafico não plotar sobre o outro

            # distribuição de frequencia
            frequencia = novo_dataframe[piloto].value_counts()
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

    # grafico de barras vertical
    def plot_ver(self, temporada):

        novo_dataframe = self.novo_dataframe(temporada) 
        
        for i,piloto in enumerate(novo_dataframe.columns):
            plt.figure(i)
            percentual = (novo_dataframe[piloto].value_counts(normalize=True) * 100).round(2)

            ax = percentual.plot.bar(width=1, alpha=0.2,figsize=(12,6))
            ax.figure.set_size_inches(12,6)
            ax.set_title(f'Distribuiçaõ de Porcentagem das Posições de {piloto}', fontsize = 16)
            ax.set_xlabel('Posições', fontsize=14)
            ax.set_ylabel('Porcentagem (%)', fontsize=14)
            # guardando imagem do grafico
            piloto = piloto.replace(" ", "")
            ax.get_figure().savefig(f'./temporadas/temporada-{temporada}/pilotos/{piloto}/porcentagem-plot-{piloto}-{temporada}.png')

    def plot_pie(self, temporada):

        novo_dataframe = self.novo_dataframe(temporada) 
    
        # grafico de pizza
        for i,piloto in enumerate(novo_dataframe.columns):
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

dist_freq = DistFreq()
temporadas = ['2006']
for temporada in temporadas:
    print(dist_freq.dist_freq(temporada))