import textwrap

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    
    [nc] Nova Conta
    [lc] Listar Conta
    [nu] Novo Usuario
    
    [q] Sair
    

    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito\tR$ {valor:.2f}\n"
        print("\nValor depositado com sucesso!")
    else:
        print("\nValor informado invalido")
    
    return saldo, extrato

def sacar (*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Você não tem saldo suficiente")
    elif excedeu_limite:
        print("O valor do saque excede o limite")
    elif excedeu_saque:
        print("Numero máximo de saques excedido")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("O valor informado é inválido")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\nExtrato")
    print("Não foram realizadas movimentações nessa conta." if not extrato else extrato)
    print("\nSaldo:\t\tR$ {saldo:.2f}")


def criar_usuario(usaurios):
    cpf = input("Informe o CPF (sem caracteres especiais):")
    usaurio = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("CPF já registrado no sistema")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado)")
    
    usaurios.append({"nome":nome,"data_nascimento": data_nascimento, "cpf": cpf})
    
    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario:")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, criação da conta cancelada")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """    
            
        print("="*100)
        print(textwrap.dedent(linha))
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            ) 
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            print("Encerrando o sistema")
            break
        else:
            print("Operação invalida")
        
    

main()
