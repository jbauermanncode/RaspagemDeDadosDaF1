from pilotos.dist_e_plots import Dist_e_plots

class GraficoPorcentagens:

    if __name__ == '__main__':
        
        temporadas = ['1981','1983','1987','1988','1990'
                    ,'1991','2005', '2006', '2007', '2008',
                    '2010', '2011', '2012', '2013','2018', 
                    '2019', '2020', '2021']

        dist_plots = Dist_e_plots()

        for temporada in temporadas:
            dist_plots.grafico_porcentagens(temporada)