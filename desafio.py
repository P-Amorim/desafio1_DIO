menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        exedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        exedeu_saques = numero_saque >= LIMITE_SAQUE

        if exedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
    
        elif exedeu_limite:
            print("Operação falhou! Você não tem o limite.")
    
        elif exedeu_saques:
            print("Operação falhou! Números máximo de saques exedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n====================== EXTRATO ==========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {valor:.2f}")
        print("===========================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")

    