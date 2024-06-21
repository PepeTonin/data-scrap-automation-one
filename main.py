from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

final_df = pd.DataFrame()
numero_de_paginas = 72
nome_arquivo_de_saida = "saida.xlsx"

for i in tqdm(range(1, numero_de_paginas + 1)):
    url = f"https://www.oabpr.org.br/servicos-consulta-de-advogados/lista-de-advogados/?nr_inscricao=0&nome=0&cidade=TOLEDO&especialidade=0&pg={i}"
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, "html.parser")
    tabela = soup.find("table")
    dados = []

    for linha in tabela.find_all("tr"):
        colunas = linha.find_all("td")
        colunas = [ele.text.strip() for ele in colunas]
        dados.append([ele for ele in colunas if ele])

    page_df = pd.DataFrame(dados)
    final_df = pd.concat([final_df, page_df])


final_df = final_df.dropna()
final_df.to_excel(nome_arquivo_de_saida, header=False, index=False)
