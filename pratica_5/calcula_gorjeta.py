"""Enunciado: Crie uma função que calcule a gorjeta a ser deixada em
um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada.
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada."""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


total_conta = float{input("insira o valor total da conta: R$ ")}
porcentagem = float{input("insira a porcentagens da gorjeta (%):  ")}

gorjeta = calcular_gorjeta(total_conta, porcentagem)

print(f'Para uma conta no valor total de R${total_conta:.2f}, a gorjeta de {porcentagem}% é {gorjeta:.2f}')