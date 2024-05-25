import textwrap

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        Cc: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))


contas = [{"agencia":'0001', "numero_conta":'1',  "usuario": {"nome": "Leo"}}]

