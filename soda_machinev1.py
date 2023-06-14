#Variaveis
usuario = ""
cedulas = ""
moedas = ""

pix = ""
lista_pagamento_pix = []
lista_telefone_pix = []
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

#funções
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
print("                                       Máquina de Refrigerante                                                  ")
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

            print("\nUnidades Disponiveis na Máquina = ", quantidade_coca)

            while controle_de_estoque !="0":
                controle_de_estoque = int(input("\n1 - Adicionar Bebida\n2 - Retirar Bebida\n3 - Voltar para a página de usuário\nDigite a o número da ação que você deseja realizar:"))
                #adicionar bebida
                if controle_de_estoque ==1:
                    adicao_bebida = int(input("Digite o número de bebidas que você quer adicionar:"))
                    quantidade_coca=quantidade_coca+adicao_bebida
                #retirar bebida
                elif controle_de_estoque==2:
                    retirar_bebida = int(input("Digite o número de bebidas que você quer retirar:"))
                    if retirar_bebida>quantidade_coca:
                        print("COCA INSUFICIENTE!")
                    else:
                        quantidade_coca=quantidade_coca-retirar_bebida
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
            print("Coca-cola: R$6,00 Reais")

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
                                    print("Valores pagos",lista_pagamento_pix)
                                    print("Lista de telefones",lista_telefone_pix)
                                    break
                                else:
                                    print("Pagamento maior que o valor da bebida.")
                                    break
                        else: 
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
                        #seleção tipo de cedula
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
                    if pagamento < 6:
                        print("Pagamento insuficiente, faltam", (6 - pagamento), "reais\nDevolver dinheiro")
                        cedula_quantidade_2-=contador_cedula_quantidade_2
                        cedula_quantidade_5-=contador_cedula_quantidade_5
                        cedula_quantidade_10-=contador_cedula_quantidade_10
                        moeda_quantidade_25-=contador_moeda_quantidade_25
                        moeda_quantidade_50-=contador_moeda_quantidade_50
                        moeda_quantidade_1-=contador_moeda_quantidade_1

                    else:
                        valor = 6
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
                                quantidade_coca=quantidade_coca-1
                            else:
                                print("Não há troco suficiente na máquina. devolver dinheiro")  
                                moeda_quantidade_25 = moeda_inicial_quantidade_25
                                moeda_quantidade_50 = moeda_inicial_quantidade_50
                                moeda_quantidade_1 = moeda_inicial_quantidade_1
                                cedula_quantidade_2 = cedula_inicial_quantidade_2
                                cedula_quantidade_5 = cedula_inicial_quantidade_5
                                cedula_quantidade_10 = cedula_inicial_quantidade_10
                else: 
                    print("Digite opcoes válidas")
                    break

            else:
                 print(" Insira opções válidas!")
