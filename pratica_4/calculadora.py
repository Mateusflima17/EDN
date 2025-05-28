Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição,
subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com
diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja
concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.




def calculadora():
    print("Calculadora - Operações básicas (+, -, *, /)")
    
    while True:
        try:
            # Solicitação do primeiro número
            while True:
                try:
                    num1 = float(input("Digite o primeiro número: "))
                    break
                except ValueError:
                    print("Erro: Entrada inválida. Por favor, digite um número.")
            
            # Solicitação do segundo número
            while True:
                try:
                    num2 = float(input("Digite o segundo número: "))
                    break
                except ValueError:
                    print("Erro: Entrada inválida. Por favor, digite um número.")
            
            # Solicitação da operação
            while True:
                operacao = input("Digite a operação (+, -, *, /): ")
                if operacao in ['+', '-', '*', '/']:
                    break
                else:
                    print("Erro: Operação inválida. Use +, -, * ou /.")
            
            # Realização da operação
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                try:
                    resultado = num1 / num2
                except ZeroDivisionError:
                    print("Erro: Divisão por zero não é permitida. Por favor, tente novamente.")
                    continue  # Reinicia o loop para nova entrada
            
            # Se chegou aqui, a operação foi bem sucedida
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

# Chamada da função da calculadora
calculadora()