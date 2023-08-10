menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! O valor informado não é válido.")

    elif opcao == "s":
        valor = float(input("Insira o valor do saque: "))

        if valor > saldo:
            print("Operação não realizada! Não há saldo suficiente.")

        elif valor > limite:
            print("Operação não realizada! O valor a ser sacado excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação não realizada! Número máximo de saques foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Sem movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")