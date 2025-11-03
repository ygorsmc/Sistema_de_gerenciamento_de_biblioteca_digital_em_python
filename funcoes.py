"""
Módulo com funções para manipulação de arquivos.
Este módulo contém todas as operações básicas para gerenciar arquivos em um diretório.
"""

import os
import datetime
import shutil


def listar_arquivos(diretorio):
    """
    Lista todos os arquivos de um diretório organizados por extensão e ano de modificação.
    
    Como funciona:
    1. Percorre todos os itens do diretório
    2. Para cada arquivo (ignora pastas), extrai a extensão e o ano de modificação
    3. Organiza em um dicionário estruturado: extensão -> ano -> lista de arquivos
    4. Cria um ID único para cada arquivo encontrado
    
    Retorna:
        Uma lista com 2 elementos:
        [0] - Dicionário organizado: {extensão: {ano: [lista de arquivos]}}
        [1] - Lista simples com todos os arquivos e seus IDs
    """
    # Obtém lista de todos os itens no diretório
    arquivos = os.listdir(diretorio)
    
    # Dicionário que armazenará os arquivos organizados por extensão e ano
    arquivos_organizados = {}
    
    # Lista simples com todos os arquivos (usado para busca por ID)
    lista_por_id = []
    
    # Contador para gerar IDs únicos para cada arquivo
    id_contador = 1
    
    # Percorre cada item encontrado no diretório
    for arquivo in arquivos:
        # Cria o caminho completo do arquivo
        caminho_completo = os.path.join(diretorio, arquivo)
        
        # Verifica se é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_completo):
            # Separa o nome do arquivo da sua extensão
            nome_arquivo, extensao_com_ponto = os.path.splitext(arquivo)
            
            # Remove o ponto da extensão (ex: ".txt" vira "txt")
            # Se não tiver extensão, usa "sem_extensao"
            extensao = extensao_com_ponto[1:] if extensao_com_ponto else 'sem_extensao'
            
            # Obtém o ano de modificação do arquivo
            timestamp = os.path.getmtime(caminho_completo)
            data_modificacao = datetime.datetime.fromtimestamp(timestamp)
            ano = str(data_modificacao.year)
            
            # Cria a estrutura no dicionário se ainda não existir
            if extensao not in arquivos_organizados:
                arquivos_organizados[extensao] = {}
            if ano not in arquivos_organizados[extensao]:
                arquivos_organizados[extensao][ano] = []
            
            # Cria um dicionário com as informações do arquivo
            arquivo_info = {
                'id': id_contador,
                'nome': arquivo
            }
            
            # Adiciona o arquivo na estrutura organizada
            arquivos_organizados[extensao][ano].append(arquivo_info)
            
            # Adiciona o arquivo na lista simples (para busca por ID)
            lista_por_id.append(arquivo_info)
            
            # Incrementa o contador de ID
            id_contador += 1
    
    # Retorna ambas as estruturas
    return [arquivos_organizados, lista_por_id]


def mover_arquivo(caminho_origem, caminho_destino):
    """
    Move um arquivo de um local para outro.
    
    Parâmetros:
        caminho_origem: Caminho completo do arquivo a ser movido
        caminho_destino: Caminho do diretório de destino
    """
    shutil.move(caminho_origem, caminho_destino)


def copiar_arquivo(caminho_origem, caminho_destino):
    """
    Copia um arquivo de um local para outro.
    
    Parâmetros:
        caminho_origem: Caminho completo do arquivo a ser copiado
        caminho_destino: Caminho do diretório de destino
    
    Nota: Usa copy2 para preservar metadados (data de modificação, etc)
    """
    shutil.copy2(caminho_origem, caminho_destino)


def renomear_arquivo(caminho_antigo, novo_nome):
    """
    Renomeia um arquivo mantendo-o no mesmo diretório.
    
    Parâmetros:
        caminho_antigo: Caminho completo do arquivo atual
        novo_nome: Novo nome para o arquivo (apenas o nome, sem caminho)
    """
    # Extrai o diretório do caminho antigo
    diretorio = os.path.dirname(caminho_antigo)
    
    # Cria o novo caminho completo combinando diretório + novo nome
    caminho_novo = os.path.join(diretorio, novo_nome)
    
    # Renomeia o arquivo
    os.rename(caminho_antigo, caminho_novo)


def remover_arquivo(caminho_arquivo):
    """
    Remove (deleta) um arquivo permanentemente.
    
    Parâmetros:
        caminho_arquivo: Caminho completo do arquivo a ser removido
    
    ATENÇÃO: Esta operação é irreversível!
    """
    os.remove(caminho_arquivo)