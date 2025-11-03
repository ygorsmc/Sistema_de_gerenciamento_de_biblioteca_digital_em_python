"""
Sistema de Gestão de Arquivos em Python

Este programa permite gerenciar arquivos em um diretório específico com as seguintes operações:
- Listar arquivos organizados por extensão e ano
- Mover arquivos entre diretórios
- Copiar arquivos
- Remover arquivos
- Renomear arquivos
- Alterar o diretório de trabalho
"""

import os
import funcoes as fn  # Importa o módulo com as funções de manipulação

# Mostra o diretório onde o programa está sendo executado
print("Diretório atual:", os.getcwd())

# Solicita ao usuário o diretório que ele quer gerenciar
diretorio_alvo = input("Digite ou copie e cole o caminho do diretório alvo para gerenciar os Arquivos: ")

# Variável que armazena a ação escolhida pelo usuário
acao = ''

# Loop principal do programa - continua até o usuário escolher sair (opção 7)
while acao != '7':

    # Mostra qual diretório está sendo gerenciado atualmente
    print(f"\nDiretório alvo atual: {diretorio_alvo}\n")

    # Exibe o menu de opções e captura a escolha do usuário
    acao = input("Digite o número de uma ação: \n"
                 "1 - listar: lista por extensão e por ano \n"
                 "2 - mover: move um arquivo de uma pasta para outra \n"
                 "3 - copiar: copia um arquivo de uma pasta para outra \n"
                 "4 - remover: apaga um arquivo da pasta \n"
                 "5 - renomear: altera o nome de um arquivo \n"
                 "6 - alterar diretório: altera a pasta de trabalho \n"
                 "7 - sair: para fechar o programa \n"
                 "Opção: ")

    # OPÇÃO 1: Listar arquivos organizados por extensão e ano
    if acao == "1":
        # Chama a função listar_arquivos e pega o dicionário organizado [0]
        lista = fn.listar_arquivos(diretorio_alvo)[0]

        # Percorre cada extensão encontrada
        for extensao, anos in lista.items():
            print(f"{extensao} ->")

            # Percorre cada ano dentro da extensão
            for ano, arquivos in anos.items():
                print(f"  {ano} ->")

                # Percorre cada arquivo dentro do ano
                for arquivo in arquivos:
                    print(f"    id:{arquivo['id']} - nome: {arquivo['nome']}")

            # Adiciona uma linha em branco entre as extensões
            print()

    # OPÇÃO 2: Mover um arquivo
    elif acao == "2":
        # Solicita o ID do arquivo que será movido
        arquivo_a_mover = int(input("Digite o id do arquivo a mover: "))

        # Busca o nome do arquivo usando o ID (ID - 1 porque a lista começa em 0)
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_mover - 1]['nome']

        # Cria o caminho completo do arquivo (diretório + nome)
        caminho_do_arquivo = os.path.join(diretorio_alvo, nome_arquivo)

        # Solicita o diretório de destino
        caminho_de_destino = input("Digite ou copie e cole o caminho do diretório de destino: ")

        # Move o arquivo
        fn.mover_arquivo(caminho_do_arquivo, caminho_de_destino)
        print("Arquivo movido com sucesso!")

    # OPÇÃO 3: Copiar um arquivo
    elif acao == '3':
        # Solicita o ID do arquivo que será copiado
        arquivo_a_copiar = int(input("Digite o id do arquivo a copiar: "))

        # Busca o nome do arquivo usando o ID
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_copiar - 1]['nome']

        # Cria o caminho completo do arquivo
        caminho_do_arquivo = os.path.join(diretorio_alvo, nome_arquivo)

        # Solicita o diretório de destino
        caminho_de_destino = input("Digite ou copie e cole o caminho do diretório de destino: ")

        # Copia o arquivo
        fn.copiar_arquivo(caminho_do_arquivo, caminho_de_destino)
        print("Arquivo copiado com sucesso!")

    # OPÇÃO 4: Remover um arquivo
    elif acao == '4':
        # Solicita o ID do arquivo que será removido
        arquivo_a_remover = int(input("Digite o id do arquivo a remover: "))

        # Busca o nome do arquivo usando o ID
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_remover - 1]['nome']

        # Cria o caminho completo do arquivo
        caminho_do_arquivo = os.path.join(diretorio_alvo, nome_arquivo)

        # Remove o arquivo
        fn.remover_arquivo(caminho_do_arquivo)
        print("Arquivo removido com sucesso!")

    # OPÇÃO 5: Renomear um arquivo
    elif acao == '5':
        # Solicita o ID do arquivo que será renomeado
        arquivo_a_renomear = int(input("Digite o id do arquivo a renomear: "))

        # Busca o nome do arquivo usando o ID
        nome_arquivo = fn.listar_arquivos(diretorio_alvo)[1][arquivo_a_renomear - 1]['nome']

        # Cria o caminho completo do arquivo
        caminho_do_arquivo = os.path.join(diretorio_alvo, nome_arquivo)

        # Solicita o novo nome e mantém a extensão original
        # Divide o nome pelo ponto e pega a última parte (extensão)
        novo_nome = input("Digite o novo nome do arquivo: ")
        extensao_original = nome_arquivo.split('.')[-1]
        novo_nome_completo = f"{novo_nome}.{extensao_original}"

        # Renomeia o arquivo
        fn.renomear_arquivo(caminho_do_arquivo, novo_nome_completo)
        print("Arquivo renomeado com sucesso!")

    # OPÇÃO 6: Alterar o diretório de trabalho
    elif acao == '6':
        # Solicita um novo diretório alvo
        diretorio_alvo = input("Digite ou copie e cole o caminho do novo diretório alvo: ")
        print("Diretório alterado com sucesso!")

    # OPÇÃO 7: Sair do programa
    elif acao == "7":
        print("Encerrando o programa.")

    # Se o usuário digitar uma opção inválida
    else:
        print("Ação inválida. Por favor, escolha uma opção de 1 a 7.")