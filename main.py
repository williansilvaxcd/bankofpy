menu = """

[d] => Depósito
[s] => Saque
[e] => Extrato
[q] => Sair

"""
saldo = 0
numero_saques = 0
extrato = ""
LIMITE_SAQUES = 3
LIMITE = 500

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input(f"\nDigite o valor para o depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"\n+++++ Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! O valor inválido")

    elif opcao == "s":
        valor = float(input(f"Informe o valor para o saque: "))

        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > LIMITE:
            print("Valor excede o valor de R$500.00 para cada saque")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diário excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"\n----- Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor é inválido!")

    elif opcao == "e":
        print("==========EXTRATO BANCÁRIO===========")
        print("Não houve movimento!" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n==========FELIZ NATAL================")

    elif opcao == "q":
        print("Programa encerrado!")
        break

    else:
        print("Opção do menu inválida!")
