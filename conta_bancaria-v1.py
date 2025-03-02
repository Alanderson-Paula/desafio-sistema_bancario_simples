menu = """
╔═════════════════════════════════════════════╗
║               BANCO D`PAULA                 ║
╠═════════════════════════════════════════════╣
║        Selecione uma operação no menu       ║
╠═════════════════════════════════════════════╣
║        1 - SAQUE                            ║
║        2 - DEPÓSITO                         ║
║        3 - EXTRATO                          ║
║        4 - SAIR                             ║
╚═════════════════════════════════════════════╝
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('Digite o valor do saque: '))
        if valor > limite:
            print(
                f'\nO seu limite por saque é: R$ {limite:.2f}\nO valor solicitado de R$ {valor:.2f} excede o limite de saque\n')
        elif valor > saldo:
            print('\nVocê não possui saldo para realizar essa operação\n')
        elif numero_saques >= LIMITE_SAQUES:
            print(
                f'\nOperação cancelada! Você atingiu o limite de {LIMITE_SAQUES} saques por dia.\n')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque:    <= R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('\nO valor informado é inválido, operação cancelada!')
    elif opcao == '2':
        valor = float(input('Digite o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: => R$ {valor:.2f}\n'
        else:
            print('\nO valor informado é inválido, operação cancelada!')
    elif opcao == '3':
        print('\n═══════════════════ EXTRATO ══════════════════\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('═' * 46, '\n')

    elif opcao == '4':

        break

    else:
        print('\nOperação inválida, por favor selecione novamente a operação desejada.')
