# Lineup-Report

Lineup-Report é um projeto que visa monitorar os navios embarcando/carregando e desembarcando/descarregando nos principais portos do Brasil, contando atualmente com os portos de Santos e Paranaguá em seu sistema. 

O sistema permite visualizar as principais informações como nome, DUV, carga e peso, dos navios atracados, além de gerar tabelas filtradas por essas informações de acordo com o intuito do usuário.

## Instalação

### 1. Instale o Python

Certifique-se de ter o Python instalado no seu sistema. Se ainda não o tiver, você pode baixá-lo [aqui](https://www.python.org/downloads/).

### 2. Clone o Repositório

Clone este repositório para o seu ambiente local usando o seguinte comando:

```bash
git clone https://github.com/BonomoJoaoPaulo/Lineup-Report.git
cd Lineup-Report    
```

### 3. Instale as Dependências

Instale as dependências necessárias para o pleno funcionamento deste projeto usando o comando pip:
```bash
pip install -r requirements.txt
```
ou
```bash
pip3 install -r requirements.txt
```

### 4. Execute o programa e divirta-se

Entre na pasta do código fonte (/src) e execute o arquivo principal com os comandos abaixo:
```bash
cd /src
python main.py
```
ou
```bash
cd /src
python3 main.py
```

### 5. Detalhamento do projeto

Com a versão demo do Lineup-Report é possível verificar todos os navios atracados, esperados, em reatracação ou em espera dos portos de Santos e Paranaguá no Brasil.
Atualmente, é possível salvar os dados dos navios em formatos de arquivo como .json e .csv, além de filtrar os navios no porto por suas mercadorias e gerar uma tabela com o volume diário previsto por produto, sentido (exportação e importação) e porto (Paranaguá, Santos).
