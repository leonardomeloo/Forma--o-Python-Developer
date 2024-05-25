from datetime import datetime
data = datetime.today().strftime('%d/%m/%Y')

def saque(*, saldo, valor_saque, LIMITE_SAQUES, numeros_saque,extrato="", limite=500):

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
    
    return  saldo, extrato, numeros_saque