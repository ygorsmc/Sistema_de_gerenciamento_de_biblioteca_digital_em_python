''' Sistema de gestão de Arquivos em Python com funcionalidades de listar, adicionar, remover e buscar Arquivos em um diretório específico.'''

import os
import funcoes as fn # Importa o módulo de funções para manipulação de arquivos

print("Diretório atual:", os.getcwd())

diretorio_alvo = input("Digite ou copie e cole o caminho do diretório alvo para gerenciar os Arquivos: ")
#diretorio_alvo = f"{os.getcwd()}\Arquivos"

acao = ''

while acao != '7':
    ''' loop principal do programa que solicita ao usuário uma ação até que ele decida sair. '''

    # Mostra o diretório alvo atual
    print(f"\nDiretório alvo atual: {diretorio_alvo}\n")

    # Solicita ao usuário uma ação
    acao = input(str("Digite o número de uma ação: \n"
                 "1 - listar: lista por extensão e por ano \n"
                 "2 - mover: move um arquivo de uma pasta para outra \n"
                 "3 - copiar: copia um arquivo de uma pasta para outra \n"
                 "4 - remover: apaga um arquivo da pasta \n"
                 "5 - renomear: altera o nome de um arquivo \n"
                 "6 - alterar diretório: altera a pasta de trabalho \n"
                 "7 - sair: para fechar o programa "
                 ))

    if acao == "1":
        # imprime de forma organizada os arquivos no dicionário retornado pela função listar_arquivos
        lista = fn.listar_arquivos(diretorio_alvo)[0]
        for extensao, anos in lista.items():
            print(f"{extensao} ->")

            # Percorre o segundo nível (os anos)
            for ano, arquivos in anos.items():
                print(f"  {ano} ->")

                # Percorre a lista de arquivos dentro de cada ano
                for arquivo in arquivos:
                    print(f"    id:{arquivo['id']} - nome: {arquivo['nome']}")

            # Adiciona uma linha em branco para separar as extensões
            print()

    elif acao == "2": # move um arquivo de um local para outro
        arquivo_a_mover = int(input("Digite o id do arquivo a mover: "))
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_mover-1]['nome']
        caminho_do_arquivo = f"{diretorio_alvo}{'\\'}{nome_arquivo}" # variável temporária para armazenar o caminho do arquivo a ser movido
        caminho_de_destino = input("Digite ou copie e cole o caminho do diretório de destino: ")
        fn.mover_arquivo(caminho_do_arquivo, caminho_de_destino)

    elif acao == '3': # copia um arquivo de um local para outro
        arquivo_a_copiar = int(input("Digite o id do arquivo a copiar: "))
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_copiar - 1]['nome']
        caminho_do_arquivo = f"{diretorio_alvo}{'\\'}{nome_arquivo}"  # variável temporária para armazenar o caminho do arquivo a ser movido
        caminho_de_destino = input("Digite ou copie e cole o caminho do diretório de destino: ")
        fn.copiar_arquivo(caminho_do_arquivo, caminho_de_destino)

    elif acao == '4': # remove um arquivo do diretório
        arquivo_a_remover = int(input("Digite o id do arquivo a remover: "))
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_remover - 1]['nome']
        caminho_do_arquivo = f"{diretorio_alvo}{'\\'}{nome_arquivo}"  # variável temporária para armazenar o caminho do arquivo a ser removido
        fn.remover_arquivo(caminho_do_arquivo)

    elif acao == '5': # renomeia um arquivo no diretório
        arquivo_a_renomear = int(input("Digite o id do arquivo a renomear: "))
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_renomear - 1]['nome']
        caminho_do_arquivo = f"{diretorio_alvo}{'\\'}{nome_arquivo}"  # variável temporária para armazenar o caminho do arquivo a ser renomeado
        novo_nome_arquivo = f"{input("Digite o novo nome do arquivo: ")}.{nome_arquivo.split('.')[-1]}" # mantém a extensão original do arquivo
        fn.renomear_arquivo(caminho_do_arquivo, novo_nome_arquivo)

    elif acao == '6': # altera o diretório alvo
        diretorio_alvo = input("Digite ou copie e cole o caminho do novo diretório alvo: ")

    elif acao == "7": # encerra o programa
        print("Encerrando o programa.")
    else:
        print("Ação inválida.")