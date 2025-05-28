EXERCÍCIO PRÁTICO 4

www.escoladanuvem.org
​

Todos os Direitos Reservados para Escola da Nuvem. Proibida a reprodução,
distribuição, venda e compartilhamento.​

Crie um programa que solicite ao usuário que insira números
inteiros. O programa deve continuar solicitando números até
que o usuário digite 'fim'. Para cada número inserido, o
programa deve informar se é par ou ímpar. Se o usuário
inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a
quantidade de números pares e ímpares inseridos.



def contar_pares_impares():
    print("Verificador de Números Pares e Ímpares")
    print("Digite números inteiros ou 'fim' para encerrar:")
    
    pares = 0
    impares = 0
    
    while True:
        entrada = input("Digite um número: ")
        
        # Verifica se o usuário quer finalizar
        if entrada.lower() == 'fim':
            break
        
        try:
            numero = int(entrada)
            
            # Verifica se é par ou ímpar
            if numero % 2 == 0:
                print(f"{numero} é par")
                pares += 1
            else:
                print(f"{numero} é ímpar")
                impares += 1
                
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros ou 'fim'.")
    
    # Exibe o resultado final
    print("\nResumo:")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Executa o programa
contar_pares_impares()