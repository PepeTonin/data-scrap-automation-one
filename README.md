<h1 text-align="center">Automação de Data Scraping</h1>

## Descrição

Este projeto é uma solução de automação desenvolvida em Python para capturar dados de uma página web específica, realizar o parsing desses dados para extrair as informações necessárias e, finalmente, gerar um arquivo Excel com os dados capturados.

## Funcionalidades

- Captura de dados de uma página web fornecida.
- Parsing dos dados para obter apenas as informações necessárias.
- Geração de um arquivo Excel com os dados capturados.

## Tecnologias utilizadas

<img src="https://img.shields.io/badge/Python-3.11.3-blue.svg?style=flat-square" alt="python version">
<img src="https://img.shields.io/badge/Requests-2.31.0-blue.svg?style=flat-square" alt="python version">
<img src="https://img.shields.io/badge/Beautiful_Soup-4.12.2-blue.svg?style=flat-square" alt="beautiful soup version">
<img src="https://img.shields.io/badge/pandas-2.0.1-blue.svg?style=flat-square" alt="pandas version">
<img src="https://img.shields.io/badge/tqdm-4.65.0-blue.svg?style=flat-square" alt="tqdm version">

## Requisitos

Para rodar este projeto, você precisará ter o [Python 3.11](https://www.python.org/) instalado em sua máquina, além das bibliotecas [Requests](https://requests.readthedocs.io/en/latest/), [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup), [pandas](https://pandas.pydata.org/docs/#) e [tqdm](https://tqdm.github.io).

## Como utilizar

1. Clone o repositório para sua máquina local.

```bash
git clone https://github.com/PepeTonin/data-scrap-automation-one.git
```

2. Navegue até o diretório do projeto.

```bash
cd data-scrap-automation-one
```

3. Instale as dependências necessárias.

```bash
pip install requests beautifulsoup4 pandas tqdm
```

4. No código, insira a url da página web que deseja capturar os dados. (Lembrando que esse script só será capaz de capturar os dados da página que ele foi pensado para capturar).

5. Por fim, rode o código e veja os dados capturados no arquivo Excel gerado (nome do arquivo "saida.xlsx"). Para rodar o código, pode usar o script: `python main.py`.
