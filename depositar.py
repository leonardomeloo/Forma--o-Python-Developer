from datetime import datetime

data = datetime.today().strftime('%d/%m/%Y')

def depositar(saldo,valor_deposito, extrato):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"{data} Deposito: R$ {valor_deposito:.2f}\n"
    else:
        print('Operação inválida! O valor informado inválido.')
    
    return saldo, extrato
