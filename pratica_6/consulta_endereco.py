
"""
Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado."""

import requests

cep = input("Digite o CEP (apenas números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    dados = requests.get(url).json()
    print("\nInformações do CEP:")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")
except:
    print("CEP não encontrado ou erro na consulta")