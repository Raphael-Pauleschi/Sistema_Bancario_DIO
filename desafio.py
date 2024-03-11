menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""

numero_saques = 0
#Na linguagem Pyton não existem constantes, então usa-se o texto
#em caixa alta para representação
LIMITE_SAQUES = 3

valor_inserido = 0
texto_exibido = ""

while True:
    opcao = input (menu)
    if opcao == "d":
        print("Iniciando sistema de Deposito")
        valor_inserido = input("Entre com o valor: ")
        texto_exibido = f"Valor de R$ {float(valor_inserido):.2f} depositado com sucesso"
        extrato += "\n"+texto_exibido 
        print (texto_exibido)
        saldo += float(valor_inserido )

    elif opcao == "s":
        print("Iniciando sistema de Saque")
        if saldo == 0:
            print("Não há valor disponivel na conta")
        else:    
            if numero_saques <= LIMITE_SAQUES:
                valor_inserido = input("Entre com o valor: ")
                if int(valor_inserido) <= 500:
                    texto_exibido = f"Valor de R$ {float(valor_inserido):.2f} sacado com sucesso"
                    print (texto_exibido)
                    extrato += "\n"+texto_exibido 
                    saldo += float(valor_inserido)
                    numero_saques += 1
                else:
                    print("Valor excede o limite de R$ 500,00")    
            else:
                print("Limite de 3 saques diarios foi atingido, cancelando operação")    

    elif opcao == "e":  
        print(f"Extrato")
        if extrato == "":
            print("Não foram realizadas transações")
        else:
            print(extrato)
            print(f"Saldo disponivel: R$ {saldo:.2f}")    
        
    elif opcao == "q":
        print("Fechando aplicação")
        break  
    else:
        print("Operação invalida")    