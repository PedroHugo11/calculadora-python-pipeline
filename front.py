from back import Subtracao
from back import Soma
from back import Multiplicacao

opcao=1

while opcao != 0:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtração")
    print("3. Multiplicacao")


    opcao = int(input("Opção: "))
    valor1 = int(input("Digite o primeiro numero:"))
    valor2 = int(input("Digite o segundo numero:"))

    if (opcao == 1):
        result = Soma.somar(valor1, valor2)
        print(valor1 , " + " , valor2 , " = " , result, "\n")
    
    if (opcao == 2):
        result = Subtracao.subtrair(valor1, valor2)
        print(valor1 , " - " , valor2 , " = " , result, "\n")

    if (opcao == 3):
        result = Multiplicacao.multiplicar(valor1, valor2)
        print(valor1 , " * " , valor2 , " = " , result, "\n")