def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def new_user(usuarios):
    
    cpf = input('Digite seu CPF (DIGITE APENAS NUMEROS): ').replace('.','').replace('-','')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuario já existente\n')
        return
    nome = input('Digite o seu nome completo: ')
    data_nascimento = input('Digite a sua data de nascimento(dd-mm-aaaa): ')
    endereco = input('Digite seu endereço (Logradouro - Nr - Bairro - Cidade/Sigla estado): ')

    usuarios.append({"nome":nome, "cpf":cpf, "data_nascimento":data_nascimento, "endereco": endereco})

    print('USUARIO CRIADO COM SUCESSO.')



