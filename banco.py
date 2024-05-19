from datetime import datetime

data = datetime.today().strftime('%d/%m/%Y') + ' '
menu = """

[d] Depositar
[s] Sacar
[e] Extrato Deposito/Saque
[q] Sair


=>"""

saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUES = 3
while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input('Valor do deposito: '))

        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            extrato += f"{data} Deposito: R$ {valor_deposito:.2f}\n"

        else:
            print('Operação inválida! O valor informado inválido.')

    elif opcao == 's':
        valor_saque = float(input('Digite o valor que deseja sacar: R$ '))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = numeros_saque >= LIMITE_SAQUES

        excedeu_saque = valor_saque > limite

        if excedeu_saldo:
            print('Saldo insuficiente.')

        elif excedeu_limite:
            print('Quantidades de saques já foram excedidas por hoje.')

        elif excedeu_saque:
            print('Saque excedeu o valor de R$ 500.00')
           

        elif valor_saque > 0:
            saldo = saldo - valor_saque
            extrato += f"{data} Saque: R$ {valor_saque:.2f}\n"
            numeros_saque +=1
            print(f'Saldo atual: {saldo}')

    elif opcao == 'e':
        print(f"\n{'='*20} 'Extrato' {'='*20}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"{'='*51}")
    elif opcao == 'q':
        print('Finalizando acesso ao banco.')
        break
    else:
        print("Opção invalida, Por favor, digite a opção desejada.\n")