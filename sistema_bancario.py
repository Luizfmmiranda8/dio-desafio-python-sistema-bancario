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
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor que deseja depositar: "))

        if valor_deposito < 0:
            print("Não é possível depositar valores negativos!")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print("Depósito concluído!")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUE:
            valor_saque = float(input("Informe o valor que deseja sacar: "))

            if valor_saque <= 500:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"Saque: R${valor_saque:.2f}\n"
                    numero_saques += 1
                    print("Saque realizado")
                else:
                    print("Saldo insuficiente!")
            else:
                print("Valor desejado maior que o limite por saque!")
        else:
            print("Você já ultrapassou o limite")

    elif opcao == "e":
        print("EXTRATO".center(27,"*"))
        print("Nenhuma movimentação registrada" if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("*".center(27,"*"))

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor selecione uma opção válida.")