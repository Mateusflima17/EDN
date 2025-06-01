""""Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação."""

import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        chave = f"{moeda}BRL"
        
        cotacao = dados[chave]
        valor_atual = float(cotacao['bid'])
        valor_max = float(cotacao['high'])
        valor_min = float(cotacao['low'])
        atualizacao = datetime.fromtimestamp(int(cotacao['timestamp']))
        
        print(f"\nCotação {moeda}-BRL:")
        print(f"🟢 Valor atual: R$ {valor_atual:.4f}")
        print(f"🔴 Máximo: R$ {valor_max:.4f}")
        print(f"🔵 Mínimo: R$ {valor_min:.4f}")
        print(f"⏰ Última atualização: {atualizacao.strftime('%d/%m/%Y %H:%M')}")
    except Exception as e:
        print(f"Erro ao consultar: {e}")

if __name__ == "__main__":
    print("Consulta de Cotações - AwesomeAPI")
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()
    consultar_cotacao(moeda)