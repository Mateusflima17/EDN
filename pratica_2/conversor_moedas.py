'''Crie um programa que converte um valor em reais para dólares e euros. 
Use os seguintes dados: - Valor em reais: R$ 100.00 - Taxa do dólar: 
R$ 5.70 - Taxa do euro: R$ 6.40 O programa deve calcular e exibir os valores convertidos, 
arredondando para duas casas decimais.'''


valor_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40  

# Conversões
valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

# Exibição dos resultados
print(f"Valor em Reais: R${valor_reais:.2f}")
print(f"Valor em Dólares: ${valor_dolares:.2f}")
print(f"Valor em Euros: €{valor_euros:.2f}")