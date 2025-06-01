"""Crie um programa que gera uma senha aleatória com o
módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de
caracteres dessa senha aleatória."""

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Quantos caracteres deve ter a senha? "))
print("Sua senha gerada é:", gerar_senha(tamanho))