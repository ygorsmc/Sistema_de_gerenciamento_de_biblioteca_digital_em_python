# Sistema de Gerenciamento de Arquivos

## 📖 Sobre o Projeto

Este é um sistema de gerenciamento de arquivos desenvolvido em Python, projetado para facilitar a organização e manipulação de documentos digitais através de uma interface de linha de comando (CLI) intuitiva e interativa.

O sistema permite executar operações essenciais de gestão de arquivos em qualquer diretório, organizando-os automaticamente por tipo (extensão) e ano de modificação, tornando a catalogação e o acesso aos documentos mais eficientes e menos propensos a erros.

## ✨ Funcionalidades

O sistema oferece seis operações principais para gerenciamento de arquivos:

1. **Listar Arquivos**: Exibe todos os arquivos do diretório organizados hierarquicamente por extensão e ano de modificação, com IDs únicos para fácil referência
2. **Mover Arquivos**: Transfere arquivos selecionados para outro diretório
3. **Copiar Arquivos**: Cria cópias de arquivos em diretórios de destino
4. **Remover Arquivos**: Exclui permanentemente arquivos do diretório
5. **Renomear Arquivos**: Altera nomes de arquivos mantendo automaticamente a extensão original
6. **Alterar Diretório**: Permite trocar o diretório de trabalho sem reiniciar o programa

## 🛠️ Estrutura do Projeto

O projeto está organizado em dois módulos para garantir separação de responsabilidades:

```
projeto/
│
├── funcoes.py                      # Módulo com todas as funções de manipulação de arquivos
├── script.py                       # Script principal com a interface CLI
├── documentacao_detalhada.md       # Esta documentação
├── relatorio_testes_feedback.md    # Relatório de testes e feedback dos bibliotecários
└── README.md                       # Documentação do projeto
```

### Módulos

**`funcoes.py`** - Biblioteca de funções centralizadas:
- `listar_arquivos()`: Lista e organiza arquivos por extensão e ano
- `mover_arquivo()`: Move arquivos entre diretórios
- `copiar_arquivo()`: Copia arquivos preservando metadados
- `renomear_arquivo()`: Renomeia arquivos no mesmo diretório
- `remover_arquivo()`: Remove arquivos permanentemente

**`script.py`** - Interface do usuário:
- Loop principal interativo
- Captura e validação de entradas do usuário
- Integração com as funções do módulo `funcoes.py`

## 🚀 Como Usar

### Pré-requisitos

- Python 3.6 ou superior instalado no sistema

### Instalação e Execução

1. Clone este repositório:
```bash
git clone <url-do-repositorio>
cd <nome-do-diretorio>
```

2. Execute o script principal:
```bash
python script.py
```

3. Insira o caminho do diretório que deseja gerenciar:
```
Digite ou copie e cole o caminho do diretório alvo para gerenciar os Arquivos: 
C:\Users\SeuUsuario\Documentos\Biblioteca
```

4. Utilize o menu interativo para executar as operações desejadas.

## 📋 Exemplos de Uso

### Menu Principal

```
Digite o número de uma ação:
1 - listar: lista por extensão e por ano
2 - mover: move um arquivo de uma pasta para outra
3 - copiar: copia um arquivo de uma pasta para outra
4 - remover: apaga um arquivo da pasta
5 - renomear: altera o nome de um arquivo
6 - alterar diretório: altera a pasta de trabalho
7 - sair: para fechar o programa
```

### Exemplo 1: Listando Arquivos

```
pdf ->
  2024 ->
    id:1 - nome: tese_final.pdf
    id:2 - nome: artigo_cientifico.pdf
  2023 ->
    id:3 - nome: livro_digital.pdf

epub ->
  2024 ->
    id:4 - nome: romance_classico.epub

txt ->
  2025 ->
    id:5 - nome: notas_pesquisa.txt
```

### Exemplo 2: Movendo um Arquivo

```
Digite o id do arquivo a mover: 1
Digite ou copie e cole o caminho do diretório de destino: 
C:\Users\SeuUsuario\Documentos\Biblioteca\Processados
```

O arquivo `tese_final.pdf` será movido para o diretório especificado.

### Exemplo 3: Renomeando um Arquivo

```
Digite o id do arquivo a renomear: 2
Digite o novo nome do arquivo: artigo_neurociencia_2024
```

O arquivo `artigo_cientifico.pdf` será renomeado para `artigo_neurociencia_2024.pdf`, mantendo a extensão original.

### Exemplo 4: Copiando um Arquivo

```
Digite o id do arquivo a copiar: 4
Digite ou copie e cole o caminho do diretório de destino: 
C:\Users\SeuUsuario\Documentos\Backup
```

Uma cópia de `romance_classico.epub` será criada no diretório de backup.

## 🔧 Detalhes Técnicos

### Dependências

O projeto utiliza apenas bibliotecas padrão do Python:
- `os`: Operações com sistema de arquivos e caminhos
- `shutil`: Operações de alto nível para cópia e movimentação de arquivos
- `datetime`: Extração de datas de modificação dos arquivos

### Sistema de IDs

Os arquivos recebem IDs sequenciais únicos a cada execução da função de listagem, facilitando a seleção em operações subsequentes sem necessidade de digitar nomes completos.

### Tratamento de Erros

Todas as funções de manipulação de arquivos incluem tratamento de exceções, exibindo mensagens informativas em caso de problemas como arquivos não encontrados ou permissões insuficientes.

## ⚠️ Observações Importantes

- **Operação de remoção**: A exclusão de arquivos é permanente. Use com cautela.
- **Caminhos de diretório**: Em sistemas Windows, use barras invertidas (`\`) ou barras normais (`/`). Em sistemas Unix/Linux/Mac, use barras normais (`/`).
- **Permissões**: Certifique-se de ter permissões adequadas para executar operações nos diretórios especificados.


## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

**Desenvolvido em Python 🐍**
