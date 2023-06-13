
pix = ""
lista_pagamento_pix = []
lista_telefone_pix = []
opcao_pagamento_usuario = ""
while opcao_pagamento_usuario!=0:
    acao = int(input("1 - pagamento pix\n2 - pagamento dinheiro\n3 - sair\n Digite uma das opções:"))
    if acao == 1:
        acao_pix = int(input("1 - realizar o pagamento\n2 - sair \n Digite uma das opções:"))
        while pix!=0:
            if acao_pix==1:
                    pagamento_pix = int(input("Digite o valor a ser pago: "))
                    if pagamento_pix < 6:
                        print("Pagamento insuficiente")
                        break
                    elif pagamento_pix == 6:
                        lista_pagamento_pix .append(pagamento_pix)
                        numero_celular = int(input("Digite seu numero de telefone: "))
                        lista_telefone_pix.append(numero_celular)
                        print("Pagamento realizado com sucesso")
                        break
                    else:
                        print("Pagamento maior que o valor da bebida.")
                        break
            else: break
    elif acao ==2:
        print("Pagamento dinheiro")
    else: 
        print("Digite opcoes válidas")
        break
    print(lista_pagamento_pix )
    print(lista_telefone_pix)
