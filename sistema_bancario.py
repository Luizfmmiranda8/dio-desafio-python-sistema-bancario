import textwrap

def menu():
    menu = """\n
    =================== MENU ===================


    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [0]\tSair


    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito < 0:
        print("\n@@@ Não é possível depositar valores negativos! @@@")
    else:
        saldo += valor_deposito
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print("\n=== Depósito concluído! ===")

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor_saque > 0:
            if valor_saque <= limite:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"Saque: R${valor_saque:.2f}\n"
                    numero_saques += 1
                    print("\n=== Saque realizado! ===")
                else:
                    print("\n@@@ Saldo insuficiente! @@@")
            else:
                print("\n@@@ Valor desejado maior que o limite por saque! @@@")
        else:
            print("\n@@@ O valor informado é invalido! @@@")
    else:
        print("\n @@@Você já ultrapassou o limite diário de saques! @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(27,"*"))
    print("Nenhuma movimentação registrada" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("*".center(27,"*"))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário cadastrado com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/ESTADO): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado! Tente novamente. @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def main():
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor_deposito = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)
            
        elif opcao == "2":
            valor_saque = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUE,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)            

        elif opcao == "0":
            break

        else:
            print("Operação inválida! Por favor selecione uma opção válida.")

main()