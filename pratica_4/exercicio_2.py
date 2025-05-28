def registrar_notas():
    print("Registro de Notas da Turma")
    print("Digite as notas dos alunos (0 a 10) ou 'fim' para terminar:")
    
    notas = []
    
    while True:
        entrada = input("Digite uma nota: ")
        
        # Verifica se o usuário quer finalizar
        if entrada.lower() == 'fim':
            break
        
        try:
            nota = float(entrada)
            
            # Verifica se a nota está no intervalo válido
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} registrada com sucesso.")
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números ou 'fim'.")
    
    # Calcula e exibe a média se houver notas registradas
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nTotal de notas registradas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

# Executa o programa
registrar_notas()