# Função para realizar a adição
def adicao(x, y):
    return x + y

# Função para realizar a subtração
def subtracao(x, y):
    return x - y

# Função para realizar a multiplicação
def multiplicacao(x, y):
    return x * y

# Função para realizar a divisão
def divisao(x, y):
    if y == 0:
        return "Divisão por zero não é permitida."
    return x / y

# Menu da calculadora
while True:
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Calculadora encerrada.")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida. Tente novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado:", divisao(num1, num2))
        