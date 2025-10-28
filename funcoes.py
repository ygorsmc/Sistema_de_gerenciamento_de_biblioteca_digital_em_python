'''Módulo com funções para manipulação de arquivos.'''

import os
import datetime
import shutil


# Função para listar Arquivos no diretório
def listar_arquivos(diretorio):
    ''' cria um dicionário com todos os rrquivos no diretório especificado por extensão e por ano, e cria um id para cada arquivo.'''
    try:
        arquivos = os.listdir(diretorio)
        arquivos_organizados = {}
        id_arquivo = []
        id_contador = 1

        for arquivo in arquivos:
            caminho_completo_arquivo = os.path.join(diretorio, arquivo)

            if os.path.isfile(caminho_completo_arquivo):
                nome_arquivo, extensao_com_ponto = os.path.splitext(arquivo)
                extensao = extensao_com_ponto[1:] if extensao_com_ponto else 'sem_extensao'

                ano = 'Desconhecido'
                try:
                    timestamp = os.path.getmtime(caminho_completo_arquivo)
                    data_modificacao = datetime.datetime.fromtimestamp(timestamp)
                    ano = str(data_modificacao.year)  # Extrai o ano corretamente

                except Exception:
                    pass

                if extensao not in arquivos_organizados:
                    arquivos_organizados[extensao] = {}
                if ano not in arquivos_organizados[extensao]:
                    arquivos_organizados[extensao][ano] = []

                arquivo_info = {
                    'id': id_contador,
                    'nome': arquivo,
                }
                arquivos_organizados[extensao][ano].append(arquivo_info)
                id_arquivo.append(arquivo_info)
                id_contador += 1

        return [arquivos_organizados, id_arquivo]

    except FileNotFoundError:
        print("Diretório não encontrado.")
        return {}


# Função para mover arquivos
def mover_arquivo(caminho_origem, caminho_destino):
    ''' move um arquivo de um local para outro.'''
    try:
        shutil.move(caminho_origem, caminho_destino)
    except Exception as e:
        print(f"Erro ao mover o arquivo {caminho_origem} para {caminho_destino}: {e}")

# Função para copiar arquivos
def copiar_arquivo(caminho_origem, caminho_destino):
    ''' copia um arquivo de um local para outro.'''
    try:
        shutil.copy2(caminho_origem, caminho_destino)
    except Exception as e:
        print(f"Erro ao copiar o arquivo {caminho_origem} para {caminho_destino}: {e}")

# Função para renomear arquivos
def renomear_arquivo(caminho_antigo, novo_nome):
    ''' renomeia um arquivo.'''
    try:
        diretorio = os.path.dirname(caminho_antigo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
    except Exception as e:
        print(f"Erro ao renomear o arquivo {caminho_antigo} para {novo_nome}: {e}")

# Função para remover arquivos
def remover_arquivo(caminho_arquivo):
    ''' remove um arquivo.'''
    try:
        os.remove(caminho_arquivo)
    except Exception as e:
        print(f"Erro ao remover o arquivo {caminho_arquivo}: {e}")
