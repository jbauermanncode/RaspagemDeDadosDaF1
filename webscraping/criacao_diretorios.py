from pathlib import Path
import os


class Diretorio:

    def criar_diretorio_dataframe(self, nome_diretorio):
        diretorio = f'./{nome_diretorio}'
        if Path(diretorio).is_dir():
            print('O diretório já existe!')
        else:
            os.mkdir(diretorio)
        

    def criar_diretorio_temporada(self, temporada):
        
        #criando diretório da temporada
        diretorio = f'./temporadas/temporada-{temporada}'
        if Path(diretorio).is_dir():
            print('O diretório já existe!')
        else:
            os.mkdir(diretorio)
    
    def criar_diretorio_pilotos(self, temporada):
        #criando diretório dos pilotos
        diretorio = f'./temporadas/temporada-{temporada}/pilotos'
        if Path(diretorio).is_dir():
            print('O diretório já existe!')
        else:
            os.mkdir(diretorio)

    def criar_diretorio_equipes(self, temporada):
        #criando diretório das equipes
        diretorio = f'./temporadas/temporada-{temporada}/equipes'
        if Path(diretorio).is_dir():
            print('O diretório já existe!')
        else:
            os.mkdir(diretorio)
    
    def criar_diretorio_para_cada_piloto(self, temporada, piloto):
        diretorio = f'./temporadas/temporada-{temporada}/pilotos/{piloto}'
        if Path(diretorio).is_dir():
            print('O diretório já existe!')
        else:
            os.mkdir(diretorio)