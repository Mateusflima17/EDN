

"""Crie um programa que gera um perfil de usuário aleatório usando a
API 'Random User Generator'. O programa deve exibir o nome, email
e país do usuário gerado."""

import requests

url = 'https://randomuser.me/api/'
dados = requests.get(url).json()
usuario = dados['results'][0]

print(f"Nome: {usuario['name']['first']} {usuario['name']['last']}")
print(f"Email: {usuario['email']}")
print(f"País: {usuario['location']['country']}")