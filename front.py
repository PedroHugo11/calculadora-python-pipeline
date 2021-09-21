from back import Subtracao

opcao=1

while opcao != 0:
    print("0. Sair")
    print("2. Subtração")


    opcao = int(input("Opção: "))
    valor1 = int(input("Digite o primeiro numero:"))
    valor2 = int(input("Digite o segundo numero:"))

    if (opcao == 2):
        result = Subtracao.subtrair(valor1, valor2)
        print(valor1 , " - " , valor2 , " = " , result, "\n")