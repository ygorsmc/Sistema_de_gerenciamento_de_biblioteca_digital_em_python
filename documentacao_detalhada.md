# 📁 Documentação do Sistema de Gestão de Arquivos

## Índice
1. [Visão Geral](#visão-geral)
2. [Requisitos](#requisitos)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Iniciando o Programa](#iniciando-o-programa)
5. [Funcionalidades Detalhadas](#funcionalidades-detalhadas)
6. [Exemplos de Uso](#exemplos-de-uso)
7. [Perguntas Frequentes](#perguntas-frequentes)

---

## Visão Geral

Este sistema foi desenvolvido em Python para facilitar o gerenciamento de arquivos em diretórios do seu computador. Ele oferece uma interface de linha de comando (CLI) simples e intuitiva para realizar operações comuns como listar, mover, copiar, remover e renomear arquivos.

### Principais Características
- ✅ Interface simples via terminal
- ✅ Listagem organizada por extensão e ano de modificação
- ✅ Sistema de IDs para identificação rápida de arquivos
- ✅ Operações de gerenciamento completas
- ✅ Possibilidade de alterar o diretório de trabalho

---

## Requisitos

### Software Necessário
- **Python 3.x** (testado em Python 3.6+)
- Bibliotecas padrão do Python:
  - `os` (manipulação de sistema de arquivos)
  - `datetime` (manipulação de datas)
  - `shutil` (operações de alto nível com arquivos)

### Sistema Operacional
- ✅ Windows
- ✅ Linux
- ✅ macOS

---

## Estrutura do Projeto

```
projeto/
│
├── script.py          # Arquivo principal do programa
├── funcoes.py         # Módulo com funções de manipulação
└── README.md          # Esta documentação
```

### Descrição dos Arquivos

**script.py**
- Arquivo principal que contém a interface do usuário
- Gerencia o loop principal do programa
- Processa as escolhas do usuário
- Chama as funções do módulo `funcoes.py`

**funcoes.py**
- Módulo auxiliar com todas as funções de manipulação
- Contém a lógica de negócio das operações
- Funções: listar, mover, copiar, renomear e remover arquivos

---

## Iniciando o Programa

### Passo 1: Executar o Script
Abra o terminal na pasta do projeto e execute:

```bash
python script.py
```

### Passo 2: Informar o Diretório
Quando solicitado, digite ou cole o caminho completo do diretório que deseja gerenciar:

**Exemplo Windows:**
```
C:\Users\SeuNome\Documents\MeusProjetos
```

**Exemplo Linux/macOS:**
```
/home/seunome/documentos/meusprojetos
```

### Passo 3: Escolher uma Ação
O menu principal será exibido com as opções de 1 a 7.

---

## Funcionalidades Detalhadas

### 1️⃣ Listar Arquivos

**O que faz:**
Lista todos os arquivos do diretório atual organizados por extensão e ano de modificação, atribuindo um ID único a cada arquivo.

**Como usar:**
1. Digite `1` no menu principal
2. O sistema exibirá os arquivos no seguinte formato:

```
txt ->
  2024 ->
    id:1 - nome: relatorio.txt
    id:2 - nome: anotacoes.txt
  2023 ->
    id:3 - nome: backup.txt

pdf ->
  2024 ->
    id:4 - nome: manual.pdf
```

**Detalhes técnicos:**
- Organização hierárquica: Extensão → Ano → Arquivos
- IDs sequenciais começando em 1
- Ano baseado na data de última modificação do arquivo
- Arquivos sem extensão aparecem como "sem_extensao"

**Quando usar:**
- Para visualizar todos os arquivos disponíveis
- Para descobrir o ID de um arquivo antes de realizar operações
- Para ter uma visão organizada do seu diretório

---

### 2️⃣ Mover Arquivo

**O que faz:**
Move um arquivo do diretório atual para outro diretório de destino. O arquivo é removido da origem.

**Como usar:**
1. Digite `2` no menu principal
2. Digite o ID do arquivo que deseja mover
3. Digite ou cole o caminho completo do diretório de destino
4. Aguarde a confirmação

**Exemplo prático:**
```
Digite o id do arquivo a mover: 3
Digite ou copie e cole o caminho do diretório de destino: C:\Backup
Arquivo movido com sucesso!
```

**Detalhes técnicos:**
- Utiliza a função `shutil.move()`
- Remove o arquivo da origem após mover
- Mantém todos os metadados do arquivo (data de criação, permissões, etc)

**Quando usar:**
- Para reorganizar arquivos entre pastas
- Para fazer backup movendo arquivos
- Para limpar diretórios movendo arquivos antigos

**⚠️ Atenção:**
- O arquivo será removido da pasta original
- Certifique-se de que o diretório de destino existe
- Se já existir um arquivo com o mesmo nome no destino, ele será substituído

---

### 3️⃣ Copiar Arquivo

**O que faz:**
Cria uma cópia exata do arquivo em outro diretório. O arquivo original permanece intacto.

**Como usar:**
1. Digite `3` no menu principal
2. Digite o ID do arquivo que deseja copiar
3. Digite ou cole o caminho completo do diretório de destino
4. Aguarde a confirmação

**Exemplo prático:**
```
Digite o id do arquivo a copiar: 1
Digite ou copie e cole o caminho do diretório de destino: D:\Backup
Arquivo copiado com sucesso!
```

**Detalhes técnicos:**
- Utiliza a função `shutil.copy2()`
- Preserva metadados (data de modificação, permissões)
- Cria uma cópia idêntica no destino
- O arquivo original permanece na origem

**Quando usar:**
- Para criar backups sem remover o original
- Para duplicar arquivos em várias pastas
- Para compartilhar arquivos mantendo uma cópia local

**⚠️ Atenção:**
- Consome espaço em disco (duplica o arquivo)
- Se já existir um arquivo com o mesmo nome no destino, ele será substituído

---

### 4️⃣ Remover Arquivo

**O que faz:**
Deleta permanentemente um arquivo do sistema.

**Como usar:**
1. Digite `4` no menu principal
2. Digite o ID do arquivo que deseja remover
3. Aguarde a confirmação

**Exemplo prático:**
```
Digite o id do arquivo a remover: 5
Arquivo removido com sucesso!
```

**Detalhes técnicos:**
- Utiliza a função `os.remove()`
- Deleta o arquivo permanentemente
- Não envia para a lixeira (remoção definitiva)

**Quando usar:**
- Para excluir arquivos desnecessários
- Para limpar espaço em disco
- Para remover arquivos temporários ou duplicados

**⚠️ ATENÇÃO - IMPORTANTE:**
- ❌ Esta operação é IRREVERSÍVEL
- ❌ O arquivo NÃO vai para a lixeira
- ❌ Não há como recuperar após a exclusão
- ✅ Sempre confirme o ID antes de executar
- ✅ Considere fazer backup antes de remover arquivos importantes

---

### 5️⃣ Renomear Arquivo

**O que faz:**
Altera o nome de um arquivo mantendo sua extensão original e localização.

**Como usar:**
1. Digite `5` no menu principal
2. Digite o ID do arquivo que deseja renomear
3. Digite apenas o NOVO NOME (sem a extensão)
4. O sistema mantém automaticamente a extensão original
5. Aguarde a confirmação

**Exemplo prático:**
```
Digite o id do arquivo a renomear: 2
Digite o novo nome do arquivo: documento_atualizado
Arquivo renomeado com sucesso!
```

Se o arquivo original era `relatorio.txt`, ele se tornará `documento_atualizado.txt`

**Detalhes técnicos:**
- Utiliza a função `os.rename()`
- Extrai automaticamente a extensão original
- Mantém o arquivo no mesmo diretório
- Preserva todos os metadados

**Quando usar:**
- Para dar nomes mais descritivos aos arquivos
- Para padronizar nomenclaturas
- Para corrigir nomes de arquivos

**⚠️ Atenção:**
- Não digite a extensão no novo nome (ela é mantida automaticamente)
- Se já existir um arquivo com o novo nome, ele será substituído
- Não use caracteres especiais inválidos (\ / : * ? " < > |)

---

### 6️⃣ Alterar Diretório

**O que faz:**
Permite mudar o diretório de trabalho sem precisar fechar e reabrir o programa.

**Como usar:**
1. Digite `6` no menu principal
2. Digite ou cole o caminho completo do novo diretório
3. Aguarde a confirmação
4. Todas as operações futuras serão realizadas no novo diretório

**Exemplo prático:**
```
Digite ou copie e cole o caminho do novo diretório alvo: C:\Users\Nome\Downloads
Diretório alterado com sucesso!

Diretório alvo atual: C:\Users\Nome\Downloads
```

**Detalhes técnicos:**
- Atualiza a variável `diretorio_alvo`
- Não valida se o diretório existe (característica atual do programa)
- Todas as operações subsequentes usam o novo caminho

**Quando usar:**
- Para gerenciar múltiplos diretórios na mesma sessão
- Para evitar reiniciar o programa
- Para trabalhar em diferentes projetos/pastas rapidamente

**💡 Dica:**
Copie e cole o caminho completo para evitar erros de digitação

---

### 7️⃣ Sair

**O que faz:**
Encerra o programa de forma limpa.

**Como usar:**
1. Digite `7` no menu principal
2. O programa exibirá "Encerrando o programa." e fechará

**Detalhes técnicos:**
- Encerra o loop principal (`while`)
- Finaliza a execução do script
- Não salva estado (o programa é stateless)

**Quando usar:**
- Quando terminar todas as operações desejadas
- Para fechar o programa adequadamente

---

## Exemplos de Uso

### Exemplo 1: Organizando Downloads

**Cenário:** Você quer organizar seus downloads movendo PDFs para uma pasta específica.

```
1. Execute: python script.py
2. Diretório: C:\Users\SeuNome\Downloads
3. Ação: 1 (listar)
4. Identifique os IDs dos PDFs
5. Para cada PDF:
   - Ação: 2 (mover)
   - ID: [número do PDF]
   - Destino: C:\Users\SeuNome\Documents\PDFs
```

---

### Exemplo 2: Backup de Documentos

**Cenário:** Criar backup de documentos importantes sem removê-los.

```
1. Execute: python script.py
2. Diretório: C:\Users\SeuNome\Documents
3. Ação: 1 (listar)
4. Para cada documento:
   - Ação: 3 (copiar)
   - ID: [número do documento]
   - Destino: D:\Backup\Documents
```

---

### Exemplo 3: Renomear Arquivos em Lote

**Cenário:** Padronizar nomes de relatórios.

```
1. Execute: python script.py
2. Diretório: C:\Projetos\Relatorios
3. Ação: 1 (listar)
4. Para cada relatório:
   - Ação: 5 (renomear)
   - ID: [número]
   - Novo nome: Relatorio_2024_[mes]
```

---

### Exemplo 4: Limpeza de Arquivos Temporários

**Cenário:** Remover arquivos temporários de um projeto.

```
1. Execute: python script.py
2. Diretório: C:\Projeto\temp
3. Ação: 1 (listar)
4. Para cada arquivo temp:
   - Ação: 4 (remover)
   - ID: [número]
```

---

### Exemplo 5: Trabalhando com Múltiplos Diretórios

**Cenário:** Organizar arquivos em diferentes pastas sem reiniciar.

```
1. Execute: python script.py
2. Diretório: C:\Pasta1
3. Realize operações em Pasta1
4. Ação: 6 (alterar diretório)
5. Novo diretório: C:\Pasta2
6. Realize operações em Pasta2
7. Repita conforme necessário
```

---

## Perguntas Frequentes

### ❓ O programa funciona em qual sistema operacional?

O programa funciona em Windows, Linux e macOS. Ele usa bibliotecas padrão do Python que são compatíveis com todos os sistemas.

---

### ❓ Posso recuperar um arquivo removido?

❌ Não. A função de remoção deleta o arquivo permanentemente. Ele não vai para a lixeira. Sempre faça backup antes de remover arquivos importantes.

---

### ❓ O que acontece se eu digitar um ID inválido?

O programa tentará acessar o arquivo correspondente ao ID. Se o ID não existir, ocorrerá um erro (como o programa não tem validação de erros por enquanto, ele encerrará).

**Solução:** Sempre liste os arquivos (opção 1) antes de realizar operações para confirmar os IDs disponíveis.

---

### ❓ Posso mover/copiar arquivos entre diferentes unidades (C:, D:, etc)?

✅ Sim! Você pode mover ou copiar arquivos entre quaisquer unidades e diretórios, desde que você tenha permissões de acesso.

---

### ❓ O programa mostra progresso para arquivos grandes?

❌ Não. A versão atual não possui barra de progresso. Para arquivos muito grandes, pode parecer que o programa travou, mas ele está processando.

---

### ❓ Posso renomear vários arquivos de uma vez?

❌ Não na versão atual. Você precisa renomear um arquivo por vez. Para renomear múltiplos arquivos, repita a operação para cada um.

---

### ❓ Como listar apenas arquivos de uma extensão específica?

A versão atual lista todos os arquivos. Você pode visualizar a organização por extensão após listar (opção 1), mas não há filtro prévio.

---

### ❓ O que significa "Desconhecido" na listagem de anos?

Significa que o sistema não conseguiu determinar o ano de modificação do arquivo. Isso é raro, mas pode acontecer com arquivos corrompidos ou com permissões especiais.

---

### ❓ Posso usar o programa para gerenciar arquivos em rede?

✅ Sim, desde que o caminho de rede esteja acessível e você tenha as permissões necessárias. Use caminhos UNC no Windows (ex: `\\servidor\pasta`).

---

### ❓ Por que o programa lista apenas arquivos e não pastas?

O programa foi projetado especificamente para gerenciar arquivos. Pastas (diretórios) são ignoradas na listagem.

---

### ❓ Posso executar o programa sem interface gráfica?

✅ Sim! O programa já é executado inteiramente via terminal/linha de comando. Não há interface gráfica.

---

### ❓ Como sair do programa rapidamente?

Digite `7` no menu principal ou pressione `Ctrl+C` para forçar o encerramento.

---

## 📞 Suporte e Contribuições

Este é um projeto educacional. Para dúvidas ou sugestões:

- Revise esta documentação
- Consulte os comentários no código
- Teste as funcionalidades em um diretório de teste antes de usar em arquivos importantes

---

## 📝 Notas de Versão

**Versão Atual:** 1.0 (Simplificada)

**Características:**
- ✅ Interface CLI funcional
- ✅ 6 operações principais
- ✅ Sistema de IDs
- ✅ Organização por extensão e ano
- ❌ Sem validação de erros
- ❌ Sem interface gráfica

**Próximas melhorias possíveis:**
- Adicionar validação de erros
- Implementar confirmação antes de remover
- Adicionar filtros de busca
- Criar logs de operações
- Interface gráfica (GUI)

---

“Durante a preparação desta Hora da Prática 2, o(s) autor(es) usaram 
Claude 4.5 para criar esse documento depois do código pronto revisado. Após usar essa ferramenta,
o(s) autor(es) revisaram e editaram o conteúdo conforme necessário e 
assumem total responsabilidade pelo conteúdo.”