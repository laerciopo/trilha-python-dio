menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
msg = ('Operação falhou! Você não tem saldo suficiente.',
       'Operação falhou! O valor do saque excede o limite.',
       'Operação falhou! Número máximo de saques excedido.',
       'Operação falhou! O valor informado é negativo.',
       'Opção inválida, por favor selecione novamente a operação desejada.'
       )

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: \tR$ {valor:.2f} (+)\n"

        else:
            print(f"{msg[3]} \nValor informado: {valor}")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > 0:

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print(f'{msg[0]} \nSaldo atual: {saldo:.2f}')
                extrato += f"\t\t\t\t\t\t << **Tentativa de saque com saldo insuficiente. ({valor}) **>>\n"

            elif excedeu_limite:
                print(f'{msg[1]} \nLimite atual: {limite:.2f}')
                extrato += f"\t\t\t\t\t\t<< **Tentativa de saque com limite por saque excedido. ({valor})** >>\n"

            elif excedeu_saques:
                print(f'{msg[2]} \nNúmero de saques permitidos: {numero_saques}')
                extrato += f"\t\t\t\t\t\t<< **Tentativa de saque após limite de {numero_saques} excedido. ** >>\n"
            else:
                saldo -= valor
                extrato += f"Saque: \t\t\t\tR$ {valor:.2f} (-)\n"
                numero_saques += 1
        else:
            print(msg[3])

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: \t\tR$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print(f'{msg[4]}')
