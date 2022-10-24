import pandas as pd
from pilotos.dataframe_invertido import DataFrameInvertido
from pilotos.modificandoPontos import ModificandoPontos
import dataframe_image as dfi

class RegulamentosDiferentes():

    dataframe = DataFrameInvertido()
    modificandoPontos = ModificandoPontos()
    

    def regulamento_2022(self, temporada):

        dataframe_invertido = self.dataframe.invertendo_dataframe(temporada)
        regulamento_2022 = self.modificandoPontos.regulamento_2022(temporada)

        # a lista a seguir criara um DataFrame com os resultados do regulamento 2022
        lista_2022 = []
        for i in dataframe_invertido.columns:
            piloto = dataframe_invertido[i].map(regulamento_2022)
            lista_2022.append(piloto)

        # criando novo DataFrame
        dataframe_2022 = pd.DataFrame(lista_2022)

        if (temporada == '1981'):

            dataframe_2022.columns

            dataframe_2022.replace({'USW': {25:26}}, inplace=True)
            dataframe_2022.replace({'BRA': {12:13}}, inplace=True)
            dataframe_2022.replace({'ARG': {25:26}}, inplace=True)
            dataframe_2022.replace({'BEL': {25:26}}, inplace=True)
            dataframe_2022.replace({'MON': {18:19}}, inplace=True)
            dataframe_2022.replace({'FRA': {25:26}}, inplace=True)
            dataframe_2022.replace({'AUT': {25:26}}, inplace=True)
            dataframe_2022.replace({'NED': {15:16}}, inplace=True)
            dataframe_2022.replace({'ITA': {15:16}}, inplace=True)
            dataframe_2022.replace({'CAN': {18:19}}, inplace=True)

        elif (temporada == '1983'):
            dataframe_2022.replace({'BRA': {25:26}}, inplace=True)
            dataframe_2022.replace({'USW': {18:19}}, inplace=True)
            dataframe_2022.replace({'FRA': {25:26}}, inplace=True)
            dataframe_2022.replace({'MON': {18:19}}, inplace=True)
            dataframe_2022.replace({'BEL': {25:26}}, inplace=True)
            dataframe_2022.replace({'DET': {15:16}}, inplace=True)
            dataframe_2022.replace({'CAN': {15:16}}, inplace=True)
            dataframe_2022.replace({'GBR': {25:26}}, inplace=True)
            dataframe_2022.replace({'GER': {25:26}}, inplace=True)
            dataframe_2022.replace({'AUT': {25:26}}, inplace=True)
            dataframe_2022.replace({'NED': {25:26}}, inplace=True)
            dataframe_2022.replace({'ITA': {25:26}}, inplace=True)
            dataframe_2022.replace({'EUR': {15:16}}, inplace=True)
            dataframe_2022.replace({'RSA': {15:16}}, inplace=True)
        
        elif (temporada == '1987'):
            dataframe_2022.replace({'BRA': {18:19}}, inplace=True)
            dataframe_2022.replace({'FRA': {18:19}}, inplace=True)
            dataframe_2022.replace({'MON': {25:26}}, inplace=True)
            dataframe_2022.replace({'BEL': {25:26}}, inplace=True)
            dataframe_2022.replace({'DET': {25:26}}, inplace=True)
            dataframe_2022.replace({'CAN': {15:16}}, inplace=True)
            dataframe_2022.replace({'GBR': {25:26}}, inplace=True)
            dataframe_2022.replace({'GER': {25:26}}, inplace=True)
            dataframe_2022.replace({'HUN': {25:26}}, inplace=True)
            dataframe_2022.replace({'AUT': {25:26}}, inplace=True)
            dataframe_2022.replace({'POR': {18:19}}, inplace=True)
            dataframe_2022.replace({'ITA': {18:19}}, inplace=True)
            dataframe_2022.replace({'MEX': {18:19}}, inplace=True)
            dataframe_2022.replace({'JPN': {18:19}}, inplace=True)
            dataframe_2022.replace({'AUS': {25:26}}, inplace=True)
        else:
            print('Não')

        # criando coluna 'Pontuação' que é a soma dos resultados de cada piloto
        dataframe_2022['Pontuação'] = dataframe_2022.sum(axis=1)
        # ordenando a coluna 'Pontuação' em ordem decrescente
        dataframe_2022 = dataframe_2022.sort_values(by='Pontuação', ascending=False)
        
        #acrescentar coluna Posição
        contador = 0
        lista_posicao = []
        while contador <= (len(dataframe_2022)-1):
            contador = contador + 1
            lista_posicao.append(contador)
        dataframe_2022.insert(0, 'Posição',lista_posicao, True)
        
        #guardando o DataFrame 
        dfi.export(dataframe_2022.head(5),f'./temporadas/temporada-{temporada}/pilotos/resultado-pilotos-regulamento-2022-{temporada}.png', table_conversion='matplotlib')

    def pole_e_volta(self, temporada):

        dataframe_invertido = self.dataframe.invertendo_dataframe(temporada)
        regulamento_volta_e_pole = self.modificandoPontos.regulamento_volta_e_pole(temporada)

        # a lista a seguir criara um DataFrame com os resultados do regulamento 2008 com acréscimo de 1ponto para pole e volta
        lista_regulamento_pole_volta_mais_rapida = []
        for i in dataframe_invertido.columns:
            piloto = dataframe_invertido[i].map(regulamento_volta_e_pole)
            lista_regulamento_pole_volta_mais_rapida.append(piloto)
        # criando novo DataFrame
        dataframe_volta_pole = pd.DataFrame(lista_regulamento_pole_volta_mais_rapida)

        if (temporada == '1981'):

            dataframe_volta_pole.replace({'USW': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'BRA': {3:4}}, inplace=True)
            dataframe_volta_pole.replace({'ARG': {9:11}}, inplace=True)
            dataframe_volta_pole.replace({'BEL': {9:11}}, inplace=True)
            dataframe_volta_pole.replace({'MON': {6:7}}, inplace=True)
            dataframe_volta_pole.replace({'ESP': {6:7}}, inplace=True)
            dataframe_volta_pole.replace({'FRA': {9:10, 3:4}}, inplace=True)
            dataframe_volta_pole.replace({'GER': {6:7}}, inplace=True)
            dataframe_volta_pole.replace({'AUT': {9:10, 6:7}}, inplace=True)
            dataframe_volta_pole.replace({'NED': {4:5, 9:10}}, inplace=True)
            dataframe_volta_pole.replace({'ITA': {4:5}}, inplace=True)
            dataframe_volta_pole.replace({'CAN': {6:7, 2:3}}, inplace=True)

        elif (temporada == '1983'):

            dataframe_volta_pole.replace({'BRA': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'USW': {6:7}}, inplace=True)
            dataframe_volta_pole.replace({'FRA': {9:11}}, inplace=True)
            dataframe_volta_pole.replace({'SAN': {4:5}}, inplace=True)
            dataframe_volta_pole.replace({'MON': {6:7, 4:5}}, inplace=True)
            dataframe_volta_pole.replace({'BEL': {9:11}}, inplace=True)
            dataframe_volta_pole.replace({'DET': {4:5}}, inplace=True)
            dataframe_volta_pole.replace({'CAN': {4:5, 9:10}}, inplace=True)
            dataframe_volta_pole.replace({'GBR': {9:10, 2:3}}, inplace=True)
            dataframe_volta_pole.replace({'GER': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'AUT': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'NED': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'ITA': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'EUR': {4:5}}, inplace=True)
            dataframe_volta_pole.replace({'RSA': {4:5}}, inplace=True)   

        elif (temporada == '1987'):   

            dataframe_volta_pole.replace({'BRA': {6:7, 1:2}}, inplace=True)
            dataframe_volta_pole.replace({'SAN': {6:7}}, inplace=True)
            dataframe_volta_pole.replace({'BEL': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'MON': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'DET': {2:3, 9:10}}, inplace=True)
            dataframe_volta_pole.replace({'FRA': {9:10, 6:7}}, inplace=True)
            dataframe_volta_pole.replace({'GBR': {6:7, 9:10}}, inplace=True)
            dataframe_volta_pole.replace({'HUN': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'AUT': {9:10, 6:7}}, inplace=True)
            dataframe_volta_pole.replace({'ITA': {9:10, 6:7}}, inplace=True)
            dataframe_volta_pole.replace({'POR': {6:8}}, inplace=True)
            dataframe_volta_pole.replace({'ESP': {3:4}}, inplace=True)
            dataframe_volta_pole.replace({'MEX': {9:10, 6:7}}, inplace=True)
            dataframe_volta_pole.replace({'JPN': {9:10}}, inplace=True)
            dataframe_volta_pole.replace({'AUS': {9:11}}, inplace=True)  

        else:
            print('Não')
        
            # criando coluna 'Pontuação' que é a soma dos resultados de cada piloto
        dataframe_volta_pole['Pontuação'] = dataframe_volta_pole.sum(axis=1)
        # ordenando a coluna 'Pontuação' em ordem decrescente
        dataframe_volta_pole = dataframe_volta_pole.sort_values(by='Pontuação', ascending=False)
        
        #acrescentar coluna Posição
        contador = 0
        lista_posicao = []
        while contador <= (len(dataframe_volta_pole)-1):
            contador = contador + 1
            lista_posicao.append(contador)
        dataframe_volta_pole.insert(0, 'Posição',lista_posicao, True)
 
        #guardando o DataFrame 
        dfi.export(dataframe_volta_pole.head(5),f'./temporadas/temporada-{temporada}/pilotos/resultado-pilotos-regulamento-volta-e-pole-{temporada}.png', table_conversion='matplotlib')

    def menos_pontos(self, temporada):

        dataframe_invertido = self.dataframe.invertendo_dataframe(temporada)
        retirando_pontos = self.modificandoPontos.retirando_pontos(temporada)
        
        lista_tirando_pontos = []
        for i in dataframe_invertido.columns:
            piloto = dataframe_invertido[i].map(retirando_pontos)
            lista_tirando_pontos.append(piloto)

            dataframe_retirando_pontos = pd.DataFrame(lista_tirando_pontos)

            # criando coluna 'Pontuação' que é a soma dos resultados de cada piloto
        dataframe_retirando_pontos['Pontuação'] = dataframe_retirando_pontos.sum(axis=1)
        # ordenando a coluna 'Pontuação' em ordem decrescente
        dataframe_retirando_pontos = dataframe_retirando_pontos.sort_values(by='Pontuação', ascending=False)

        if (temporada == '1983'):
            
            dataframe_retirando_pontos = dataframe_retirando_pontos.T
            # mudar Alain Prost e Nelson Piquet de lugar, pois Prost 
            # tinha mais vitórias e esse era o primeiro critério de desempate
            dataframe_retirando_pontos = dataframe_retirando_pontos[['Alain Prost', 'Nelson Piquet', 'René Arnoux', 'Patrick Tambay',
                'Keke Rosberg', 'John Watson', 'Eddie Cheever', 'Jonathan Palmer',
                'Jean-Louis Schlesser', 'Alan Jones', 'Chico Serra',
                'Jacques Villeneuve Sr.', 'Jacques Laffite', 'Nigel Mansell',
                'Marc Surer', 'Thierry Boutsen', 'Andrea de Cesaris',
                'Michele Alboreto', 'Stefan Johansson', 'Riccardo Patrese',
                'Niki Lauda', 'Derek Warwick', 'Eliseo Salazar', 'Kenny Acheson',
                'Johnny Cecotto', 'Danny Sullivan', 'Mauro Baldi', 'Bruno Giacomelli',
                'Raul Boesel', 'Jean-Pierre Jarier', 'Roberto Guerrero',
                'Manfred Winkelhock', 'Elio de Angelis', 'Corrado Fabi',
                'Piercarlo Ghinzani']]
            dataframe_retirando_pontos = dataframe_retirando_pontos.T
        
        elif (temporada == '2007'):
            dataframe_retirando_pontos = dataframe_retirando_pontos.T
            # mudar Alonso e Hamilton de lugar, pois Hamilton 
            # tinha mais segundos lugares e esse era o segundo critério de desempate
            dataframe_retirando_pontos = dataframe_retirando_pontos[['Lewis Hamilton','Fernando Alonso', 'Kimi Räikkönen', 'Felipe Massa',
                'Nick Heidfeld', 'Robert Kubica', 'Heikki Kovalainen',
                'Giancarlo Fisichella', 'Nico Rosberg', 'Alexander Wurz',
                'Jarno Trulli', 'Kazuki Nakajima', 'Sebastian Vettel',
                'David Coulthard', 'Takuma Sato', 'Markus Winkelhock', 'Mark Webber',
                'Rubens Barrichello', 'Sakon Yamamoto', 'Jenson Button',
                'Ralf Schumacher', 'Christijan Albers', 'Anthony Davidson',
                'Vitantonio Liuzzi', 'Adrian Sutil', 'Scott Speed']]
            dataframe_retirando_pontos = dataframe_retirando_pontos.T

        elif (temporada == '2018'):
            dataframe_retirando_pontos = dataframe_retirando_pontos.T
            # mudar 'Max Verstappen' e 'Kimi Räikkönen' de lugar, pois 'Max Verstappen'
    # tinha mais vitórias e esse era o primeiro critério de desempate
            dataframe_retirando_pontos = dataframe_retirando_pontos[['Lewis Hamilton', 'Sebastian Vettel', 'Valtteri Bottas',
                'Max Verstappen','Kimi Räikkönen',  'Daniel Ricciardo', 'Sergio Pérez',
                'Nico Hülkenberg', 'Kevin Magnussen', 'Carlos Sainz Jr.',
                'Fernando Alonso', 'Esteban Ocon', 'Charles Leclerc', 'Romain Grosjean',
                'Pierre Gasly', 'Stoffel Vandoorne', 'Lance Stroll', 'Marcus Ericsson',
                'Sergey Sirotkin', 'Brendon Hartley']]
            dataframe_retirando_pontos = dataframe_retirando_pontos.T
        
        #acrescentar coluna Posição
        contador = 0
        lista_posicao = []
        while contador <= (len(dataframe_retirando_pontos)-1):
            contador = contador + 1
            lista_posicao.append(contador)
        dataframe_retirando_pontos.insert(0, 'Posição',lista_posicao, True)

        dfi.export(dataframe_retirando_pontos.head(5),f'./temporadas/temporada-{temporada}/pilotos/resultado_pilotos_com_decrescimo_pontos_{temporada}.png', table_conversion='matplotlib')


