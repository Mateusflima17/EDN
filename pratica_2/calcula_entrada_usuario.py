''''Calculadora de Soma com Entrada do Usuário Leia 2 valores inteiros e armazene-os nas variáveis `A` e `B`. 
Efetue a soma de `A` e `B`, atribuindo o seu resultado à variável `X`. 
**Entrada:** A entrada contém **2 valores inteiros** informados pelo usuário. 
**Saída:** Imprima a mensagem `"X = "` (letra X maiúscula) seguido pelo valor da variável `X`
 e pelo final de linha.'''

# Calculadora de Soma com Entrada do Usuário

# Leitura dos valores (convertendo para inteiro)
A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))

# Cálculo da soma
X = A + B

# Exibição do resultado conforme especificado
print(f"X = {X}")