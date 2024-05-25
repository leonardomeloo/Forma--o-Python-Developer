from usuario import filtrar_usuario

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite seu CPF (DIGITE APENAS NUMEROS): ').replace('.','').replace('-','')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('CONTA CRIADA COM SUCESSO!!!')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario': usuario}
    else:
        print('Usuario não existente')
        

