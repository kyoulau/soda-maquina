#Variaveis
usuario = ""
cedulas = ""
moedas = ""

pix = ""
lista_pagamento_pix = []
lista_telefone_pix = []

lista_valor_transacao = []
lista_numero_cartao = []
lista_data_validade =[]

cartao = ""

opcao_pagamento_usuario = ""

controle_de_estoque = ""
moeda_quantidade_25 = 0
moeda_quantidade_50 = 0
moeda_quantidade_1 = 0
cedula_quantidade_2 = 3
cedula_quantidade_5 = 1
cedula_quantidade_10 = 0

moeda_inicial_quantidade_25 = moeda_quantidade_25
moeda_inicial_quantidade_50 = moeda_quantidade_50
moeda_inicial_quantidade_1 = moeda_quantidade_1
cedula_inicial_quantidade_2 = cedula_quantidade_2
cedula_inicial_quantidade_5 = cedula_quantidade_5
cedula_inicial_quantidade_10 = cedula_quantidade_10

soma_total_dinheiro_maquina = (0.25*moeda_quantidade_25) + (0.50*moeda_quantidade_50) + (1*moeda_quantidade_1) + (2*cedula_quantidade_2) + (5*cedula_quantidade_5) + (10*cedula_quantidade_10)

pagamento = 0
quantidade_coca = 40
quantidade_fanta_uva = 40
quantidade_suco_laranja = 40

#funções do troco
def calcular_troco(quantidade_dinheiro, troco, tipo_dinheiro, qtd_diminuir):
    if quantidade_dinheiro>=troco//tipo_dinheiro:
        troco = troco%tipo_dinheiro
        return troco
    else:
        troco=troco -(qtd_diminuir*tipo_dinheiro)
        return troco
    
def reduzir_dinheiro (quantidade_dinheiro, troco, tipo_dinheiro,):
    quantidade_dinheiro = quantidade_dinheiro - (troco//tipo_dinheiro)
    return quantidade_dinheiro

def diminuir_quantidade(qtd_diminuir,troco,tipo_dinheiro, quantidade_dinheiro):
    qtd_diminuir = qtd_diminuir+(troco//tipo_dinheiro)
    if qtd_diminuir<=quantidade_dinheiro:
        return qtd_diminuir
    elif (qtd_diminuir-quantidade_dinheiro)>=0:
        if quantidade_dinheiro == 0:
            qtd_diminuir = 0
            return qtd_diminuir 
        else:
            qtd_diminuir = qtd_diminuir - (qtd_diminuir-quantidade_dinheiro)
            return qtd_diminuir       
    else:
        qtd_diminuir = 0
        return qtd_diminuir
    
#print inicial e seleção de usuário
print("================================================================================================================")
print("                                       Máquina de Bebida                                                  ")
print("================================================================================================================")
print("                                       Selecione seu Usuário                                                    ")
print("================================================================================================================")

#seleção tipo de usuario 
while usuario != "0":
    usuario = int(input("1 - Administrador\n2 - Consumidor\nDigite o número do seu usuário:"))

#configurações adm
    if usuario == 1:
        senha = str(input("Insira a senha:"))
        if senha == "adm123":
            print("================================================================================================================")
            print("                                       ACESSO PERMITIDO                                                         ")
            print("================================================================================================================\n")
            print("DINHEIRO NA MÁQUINA"
            "\nR$ 0,25 =" ,moeda_quantidade_25,
            "\nR$ 0.50 =",moeda_quantidade_50,
            "\nR$ 1,00 =" ,moeda_quantidade_1,
            "\nR$ 2,00 =" ,cedula_quantidade_2,
            "\nR$ 5,00 =" ,cedula_quantidade_5,
            "\nR$ 10,00=" ,cedula_quantidade_10,)

            print("\nUnidades Disponiveis na Máquina:","\n quantidade de coca-cola =",quantidade_coca,
                  "\n quantidade de suco de laranja =", quantidade_suco_laranja,
                  "\n quantidade de fanta de uva =",quantidade_fanta_uva)

            print("\nPAGAMENTO PIX")
            print("Valores pagos por pix",lista_pagamento_pix)
            print("Lista de telefones do pagamento por pix",lista_telefone_pix)

            print("\nPAGAMENTO CARTÃO","\nlista de valores da transações:",lista_numero_cartao,"\nlista dos número dos cartões:",
                  lista_numero_cartao,"\nlista das validades dos cartões:",lista_data_validade)

            while controle_de_estoque !="0":
                controle_de_estoque = int(input("\n1 - Adicionar Bebida\n2 - Retirar Bebida\n3 - Voltar para a página de usuário\nDigite a o número da ação que você deseja realizar:"))
                #adicionar bebida
                if controle_de_estoque ==1:
                    tipo_bebida = int(input("1 - coca-cola\n2 - suco de laranja\n3 - fanta uva\nSelecione o tipo de bebida:"))
                    if tipo_bebida == 1:
                        adicao_bebida = int(input("Digite o número de bebidas que você quer adicionar:"))
                        quantidade_coca=quantidade_coca+adicao_bebida
                    elif tipo_bebida ==2:
                        adicao_bebida = int(input("Digite o número de bebidas que você quer adicionar:"))
                        quantidade_suco_laranja = quantidade_suco_laranja + adicao_bebida
                    elif tipo_bebida ==3:
                        adicao_bebida = int(input("Digite o número de bebidas que você quer adicionar:"))
                        quantidade_fanta_uva = quantidade_fanta_uva + adicao_bebida
                    else:
                        print("Insira apenas opções válidas.")
                    break
                #retirar bebida
                elif controle_de_estoque==2:
                    tipo_bebida = int(input("1 - coca-cola\n2 - suco de laranja\n3 - fanta uva\nSelecione o tipo de bebida:"))
                    if tipo_bebida ==1:
                        retirar_bebida = int(input("Digite o número de bebidas que você quer retirar:"))
                        if retirar_bebida>quantidade_coca:
                            print("Quantidade de coca insuficiente na máquina")
                        else:
                            quantidade_coca=quantidade_coca-retirar_bebida
                    elif tipo_bebida ==2:
                        retirar_bebida = int(input("Digite o número de bebidas que você quer retirar:"))
                        if retirar_bebida>quantidade_suco_laranja:
                            print("Quantidade de suco de laranja insuficiente na máquina")
                        else:
                            quantidade_suco_laranja=quantidade_suco_laranja-retirar_bebida
                    elif tipo_bebida ==3:
                        retirar_bebida = int(input("Digite o número de bebidas que você quer retirar:"))
                        if retirar_bebida>quantidade_fanta_uva:
                            print("Quantidade de fanta uva insuficiente na máquina")
                        else:
                            quantidade_fanta_uva=quantidade_fanta_uva-retirar_bebida
                    break                             
                #volta seleção do tipo de usuario
                elif controle_de_estoque==3: 
                    break
                else:
                    print("Digite apenas as opções válidas.")
        else:
            print("Senha incorreta. Tente novamente")

#configurações consumidor
    elif usuario == 2:
        if quantidade_coca<=0:
             print("Não há bebida na máquina.")
        else:
            print("================================================================================================================")
            print("                                             OPÇÕES DE BEBIDA                                                   ")
            print("================================================================================================================")
            print("1 - Coca-cola: R$6,00 Reais\n2 - Suco de laranja R$5,00 Reais\n3 - Fanta-uva R$5,50")
            #seleção de bebida
            escolha_bebida =int(input("Selecione o número da bebida:"))
            if escolha_bebida == 1:
                valor = 6
            elif escolha_bebida == 2:
                valor = 5
            elif escolha_bebida == 3:
                valor = 5.5
            else:
                print("Selecione apenas opções válidas.")

            while opcao_pagamento_usuario!=0:
                acao = int(input("1 - pagamento pix\n2 - pagamento dinheiro\n3 - cartão\n4 - sair\n Digite uma das opções:"))
                if acao == 1:
                    acao_pix = int(input("1 - realizar o pagamento\n2 - sair \n Digite uma das opções:"))
                    while pix!=0:
                        if acao_pix==1:
                                print("Valor da bebida:", valor)
                                pagamento_pix = float(input("Digite o valor a ser pago: "))
                                if pagamento_pix < valor:
                                    print("Pagamento insuficiente")
                                    break
                                elif pagamento_pix == valor:
                                    lista_pagamento_pix .append(pagamento_pix)
                                    numero_celular = int(input("Digite seu numero de telefone: "))
                                    lista_telefone_pix.append(numero_celular)
                                    print("Pagamento realizado com sucesso")
                                    if escolha_bebida ==1:
                                        quantidade_coca-=1
                                    elif escolha_bebida ==2:
                                        quantidade_suco_laranja-=1
                                    elif escolha_bebida ==3:
                                        quantidade_fanta_uva-=1
                                    break
                                else:
                                    print("Pagamento maior que o valor da bebida.")
                                    break
                        else: 
                            break
                    break
                elif acao ==2:
                    while cedulas != "0":
                        contador_moeda_quantidade_25 = 0
                        contador_moeda_quantidade_50 = 0
                        contador_moeda_quantidade_1 = 0
                        contador_cedula_quantidade_2 = 0
                        contador_cedula_quantidade_5 = 0
                        contador_cedula_quantidade_10 = 0

                        print("========== Pagamento ==========")
                        print("Pagamento atual =", pagamento)
                        cedulas = float(input("1 - R$ 0,25\n2 - R$ 0,50\n3 - R$ 1,00 \n4 - R$ 2,00 \n5 - R$ 5,00\n6 - R$ 10,00 \n7 - Finalizar pagamento\n Selecione o tipo de dinheiro que você deseja inserir: "))
                        #seleção tipo de cedula para pagamento em dinheiro
                        if cedulas == 1:
                            contador_moeda_quantidade_25+=1
                            moeda_quantidade_25+=contador_moeda_quantidade_25
                            pagamento=pagamento+0.25
                        elif cedulas == 2:
                            contador_moeda_quantidade_50+=1
                            moeda_quantidade_50+=contador_moeda_quantidade_50
                            pagamento=pagamento+0.5
                        elif cedulas == 3:
                            contador_moeda_quantidade_1+=1
                            moeda_quantidade_1+=contador_moeda_quantidade_1
                            pagamento=pagamento+1
                        elif cedulas == 4:
                            contador_cedula_quantidade_2+=1
                            cedula_quantidade_2+=contador_cedula_quantidade_2
                            pagamento=pagamento+2
                        elif cedulas == 5:
                            contador_cedula_quantidade_5+=1
                            cedula_quantidade_5+=contador_cedula_quantidade_5
                            pagamento=pagamento+5
                        elif cedulas == 6:
                            contador_cedula_quantidade_10+=1
                            cedula_quantidade_10+=contador_cedula_quantidade_10
                            pagamento=pagamento+10
                        elif cedulas == 7:
                            break
                        else:
                            print("Digite apenas as opções existentes.")
                        #pagamento insuficiente que não libera a bebida
                    if pagamento < valor:
                        print("Pagamento insuficiente, faltam", (valor - pagamento), "reais\nDevolver dinheiro")
                        cedula_quantidade_2-=contador_cedula_quantidade_2
                        cedula_quantidade_5-=contador_cedula_quantidade_5
                        cedula_quantidade_10-=contador_cedula_quantidade_10
                        moeda_quantidade_25-=contador_moeda_quantidade_25
                        moeda_quantidade_50-=contador_moeda_quantidade_50
                        moeda_quantidade_1-=contador_moeda_quantidade_1

                    else:
                        troco = pagamento - valor
                        qtd_diminuir = 0
                        #troco maior que a quantidade de dinheiro na maquina
                        if troco>soma_total_dinheiro_maquina:
                            print("Não há troco suficiente na máquina. devolver dinheiro")
                            moeda_quantidade_25 = moeda_inicial_quantidade_25
                            moeda_quantidade_50 = moeda_inicial_quantidade_50
                            moeda_quantidade_1 = moeda_inicial_quantidade_1
                            cedula_quantidade_2 = cedula_inicial_quantidade_2
                            cedula_quantidade_5 = cedula_inicial_quantidade_5
                            cedula_quantidade_10 = cedula_inicial_quantidade_10

                        else:
                            print("Pagamento total = ", pagamento)
                            print("Troco =",troco)
                            #sistema de troco
                            qtd_diminuir = diminuir_quantidade(qtd_diminuir,troco,10,cedula_quantidade_10)
                            troco = calcular_troco(cedula_quantidade_10,troco,10 ,qtd_diminuir)
                            cedula_quantidade_10 = cedula_quantidade_10 - qtd_diminuir

                            qtd_diminuir = diminuir_quantidade(qtd_diminuir,troco,5,cedula_quantidade_5)
                            troco = calcular_troco(cedula_quantidade_5,troco,5,qtd_diminuir)
                            cedula_quantidade_5 = cedula_quantidade_5 - qtd_diminuir

                            qtd_diminuir = diminuir_quantidade(qtd_diminuir,troco,2,cedula_quantidade_2)
                            troco = calcular_troco(cedula_quantidade_2,troco,2,qtd_diminuir)
                            cedula_quantidade_2 = cedula_quantidade_2 - qtd_diminuir

                            qtd_diminuir = diminuir_quantidade(qtd_diminuir,troco,1,moeda_quantidade_1)
                            troco = calcular_troco(moeda_quantidade_1,troco,1,qtd_diminuir)
                            moeda_quantidade_1 = moeda_quantidade_1 - qtd_diminuir

                            qtd_diminuir = diminuir_quantidade(qtd_diminuir,troco,0.5,moeda_quantidade_50)
                            troco = calcular_troco(moeda_quantidade_50,troco,0.5,qtd_diminuir)
                            moeda_quantidade_50 = moeda_quantidade_50 - qtd_diminuir

                            qtd_diminuir = diminuir_quantidade(qtd_diminuir,troco,0.25,moeda_quantidade_25)
                            troco = calcular_troco(moeda_quantidade_25,troco,0.25,qtd_diminuir)
                            moeda_quantidade_25 = moeda_quantidade_25 - qtd_diminuir

                            #pagamento efetuado 
                            if troco == 0:
                                print("Liberar bebida")
                                if escolha_bebida ==1:
                                    quantidade_coca-=1
                                elif escolha_bebida ==2:
                                    quantidade_suco_laranja-=1
                                elif escolha_bebida ==3:
                                    quantidade_fanta_uva-=1
                            else:
                                print("Não há troco suficiente na máquina. devolver dinheiro")  
                                moeda_quantidade_25 = moeda_inicial_quantidade_25
                                moeda_quantidade_50 = moeda_inicial_quantidade_50
                                moeda_quantidade_1 = moeda_inicial_quantidade_1
                                cedula_quantidade_2 = cedula_inicial_quantidade_2
                                cedula_quantidade_5 = cedula_inicial_quantidade_5
                                cedula_quantidade_10 = cedula_inicial_quantidade_10
                    break
                elif acao ==3:
                    print("Valor total:", valor, "R$ reais")
                    valor_transacao = float(input("Digite o valor da transação: "))
                    lista_valor_transacao.append(valor_transacao)
                    if valor_transacao!= valor:
                        print("Valor da transação incorreto.")
                        lista_valor_transacao.pop()
                    else:
                        numero_cartao = input("Digite o número do cartão: ")
                        lista_numero_cartao.append(numero_cartao)
                        data_validade = input("Digite a data de validade: ")
                        lista_data_validade.append(data_validade)
                        print("\n Realizando pagamento....")
                        validacao_retirada_cartao = 2
                        while validacao_retirada_cartao != 3:
                            remocao = int(input("Retire o cartão\n Digite [1] para simular:"))
                            if remocao == 1:
                                True
                                validacao_retirada_cartao =3
                                print("Transação realizada com sucesso !")
                                if escolha_bebida ==1:
                                    quantidade_coca-=1
                                elif escolha_bebida ==2:
                                    quantidade_suco_laranja-=1
                                elif escolha_bebida ==3:
                                    quantidade_fanta_uva-=1
                        break
                elif acao==4:
                    break
                else: 
                    print("Digite opcoes válidas")
                    break
            else:
                 print(" Insira opções válidas!")
