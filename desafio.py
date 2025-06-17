### Desafio - Refatorar o projeto da aula anterior evitando Bugs!


CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
try:
    nome_usuario = input("Digite o seu nome: ")
    if nome_usuario.isdigit():
        print("Você digitou seu nome errado")
        exit()
    elif len(nome_usuario) == 0:
        print("Você não digitou nada!")
        exit()
    elif nome_usuario.isspace():
        print("Você digitou só espaços")
        exit()
except ValueError as e:
    print(e)
    exit()


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite o seu salario: "))
    if salario_usuario < 0:
        print("Por favor, digite um numero positivo para o salário")
        exit()
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuario = float(input("Digite o seu bonus: "))
    if bonus_usuario < 0:
        print("Por favor, você precisa digitar um número positivo para o bônus")
        exit()
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()


# 4) Calcule o valor do bônus final
try:
    valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
except ZeroDivisionError:
    print("Erro de divisão por zero")

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")
