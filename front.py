from back import Soma

opcao=1

while opcao != 0:
    print("0. Sair")
    print("1. Somar")


    opcao = int(input("Opção: "))
    valor1 = int(input("Digite o primeiro numero:"))
    valor2 = int(input("Digite o segundo numero:"))

    if (opcao == 1):
        result = Soma.somar(valor1, valor2)
        print(valor1 , " + " , valor2 , " = " , result, "\n")