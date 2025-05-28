EXERCÍCIO PRÁTICO 3

www.escoladanuvem.org
​

Todos os Direitos Reservados para Escola da Nuvem. Proibida a reprodução,
distribuição, venda e compartilhamento.​

Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'.

python
def verificar_senha_forte():
    print("Verificador de Senha Forte")
    print("Critérios para senha forte:")
    print("- Pelo menos 8 caracteres")
    print("- Pelo menos 1 número")
    print("Digite 'sair' para encerrar o programa\n")
    
    while True:
        senha = input("Digite uma senha para verificação: ")
        
        # Verifica se o usuário quer sair
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        # Verifica o comprimento da senha
        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres")
            continue
        
        # Verifica se contém pelo menos um número
        tem_numero = any(caractere.isdigit() for caractere in senha)
        if not tem_numero:
            print("Senha fraca: deve conter pelo menos um número")
            continue
        
        # Se passou em todas as verificações
        print("Senha forte! Atendendo a todos os critérios.")
        break

# Executa o programa
verificar_senha_forte()