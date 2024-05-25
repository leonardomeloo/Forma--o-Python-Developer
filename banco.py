from datetime import datetime
from depositar import depositar
from saque import saque
from extrato import mostrar_extrato
from usuario import new_user
from criar_conta import criar_conta
from listar_contas import listar_contas

data = datetime.today().strftime('%d/%m/%Y') + ' '
menu = """

[d] Depositar
[s] Sacar
[e] Extrato Deposito/Saque
[nu] Criar usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair


=>"""
AGENCIA = '0001'
saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input('Valor do deposito: '))
        saldo, extrato = depositar(saldo, valor_deposito, extrato)
       
    elif opcao == 's':
        valor_saque = float(input('Digite o valor que deseja sacar: R$ '))
        saldo, extrato, numeros_saque = saque(saldo=saldo,
                                               valor_saque=valor_saque, 
                                               LIMITE_SAQUES=LIMITE_SAQUES,
                                                 numeros_saque=numeros_saque, 
                                                 extrato=extrato, 
                                                 limite=limite)
        
    elif opcao == 'e':
       mostrar_extrato(saldo, extrato=extrato)

    elif opcao == 'q':
        print('Finalizando acesso ao banco.')
        break

    elif opcao == 'nu':
        new_user(usuarios)
    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
    elif opcao == 'lc':
        listar_contas(contas)
    else:
        print("Opção invalida, Por favor, digite a opção desejada.\n")