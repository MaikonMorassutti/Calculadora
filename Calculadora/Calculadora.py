# Fun��o para realizar a adi��o
def adicao(x, y):
    return x + y

# Fun��o para realizar a subtra��o
def subtracao(x, y):
    return x - y

# Fun��o para realizar a multiplica��o
def multiplicacao(x, y):
    return x * y

# Fun��o para realizar a divis�o
def divisao(x, y):
    if y == 0:
        return "Divis�o por zero n�o � permitida."
    return x / y

# Menu da calculadora
while True:
    print("Escolha a opera��o:")
    print("1. Adi��o")
    print("2. Subtra��o")
    print("3. Multiplica��o")
    print("4. Divis�o")
    print("5. Sair")

    escolha = input("Digite o n�mero da opera��o desejada: ")

    if escolha == '5':
        print("Calculadora encerrada.")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Op��o inv�lida. Tente novamente.")
        continue

    num1 = float(input("Digite o primeiro n�mero: "))
    num2 = float(input("Digite o segundo n�mero: "))

    if escolha == '1':
        print("Resultado:", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado:", divisao(num1, num2))
        