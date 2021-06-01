import random
import time
import sys
import CasaModulo
import EventosModulo
import PersonagemModulo
import RelogioModulo

if(__name__ == "__main__"):
    dia = 1
    relogio = RelogioModulo.Relogio()
    personagem = PersonagemModulo.Personagem(15)
    casa = CasaModulo.Casa()
    eventos = EventosModulo.Eventos()
    cafe_da_manha = False
    print('-=-'*15, '\n         Bem vindo ao JOGO DA VIDA.')
    print('-=-'*15)    
    print('                 ATENÇÃO!!!')
    print('5 advertências você perde o emprego;')
    print('5 elogios você recebe uma promoção, aumento salarial e redução de uma advertência.')
    print('Se zerar seu HP, você perde o jogo!')
    print('Se zerar seu caixa, você perde o jogo!')
    print('Se conseguir juntar R$1000.00, você automaticamente ganha o jogo!')
    print('Ao fim de cada dia, um valor é descontado do seu caixa para pagar o alguel!')
    print('-=-'*15)
    print('          Tabela de Advertências:') 
    print('- Receber reclamação no trabalho: 1  ')
    print('- Chegar atrasado no trabalho: 1  ')
    print('- Faltar o trabalho: 2')
    print('-=-'*15)
    if input('Digite 1 para criar seu personagem ou 2 para ser padrão: ') == '1': personagem.montar_personagem()
    print('-=-'*15)
    while True:
        if personagem.dinheiro >= 1000:
            print("Parabéns, você ganhou o jogo da vida! :D")
            sys.exit()
        if personagem.dinheiro <= 0:
            print("Você ficou sem dinheiro, teve que ir morar na rua e agora é indigente, espero que seu corpo ajude nas pesquisas de laboratório das faculdade :D")
            sys.exit()
        if personagem.HP <= 0:
            print("-=-"*15)
            print("Você morreu, tente novamente!")
            print("-=-"*15)
            sys.exit()
        if personagem.advertencia >= 5:
            print('-=-'*15)
            print('Você foi DEMITIDO pois recebeu 5 advertências. Agora não irá mais receber dinheiro por dia.')
            print('-=-'*15)
            personagem.demitido = True
            personagem.advertencia = 0
        elif personagem.elogio >= 5:
            personagem.salario = (personagem.salario + 50)
            print('-=-'*15)
            print(f'Você foi PROMOVIDO!!! Parabéns! Seu salário agora é {personagem.salario}')
            print('-=-'*15)
            personagem.elogio = 0
            if personagem.advertencia >= 1:
                personagem.advertencia -= 1
        while personagem.acordado == False:               
            eventos.menu_bomdia_padrao()              
            opcao = input("Escolha sua ação: ") 
            if(opcao == "1"):
                personagem.acordado = True
            elif(opcao == "2"):
                sorte_sono = random.randint(1,12)
                if(sorte_sono <= 8):
                    print('-=-'*15)
                    print("Ok, durma mais um pouco...")
                    time.sleep(0.5)
                    relogio.avancaTempo(5)
                    print('-=-'*15)
                    print("Agora são "+str(relogio)+".\n")                    
                else:
                    time.sleep(0.5)
                    if personagem.demitido == False:
                        print('-=-'*15)
                        print("Você dormiu mais do que o necessário e agora está atrasadíssimo!\n")
                        personagem.acordado = True
                        relogio.avancaTempo(45)
                        if relogio.horas >= 7:
                            personagem.atrasado = True
                    else:
                        print('-=-'*15)
                        print("Você dormiu bastante guerreiro, vá atrás de um trabalho!")
                        personagem.acordado = True
                        relogio.avancaTempo(120)
                    break
            elif(opcao == "0"):
                sys.exit()
            else:
                print("Opção inválida!")
                continue
        
        if personagem.demitido == False:
            if (personagem.atrasado == True):
                print(str(personagem.nome)+" são "+str(relogio)+" do dia "+str(dia)+". Você tinha que sair pro trabalho até as 07:00.\n")
                eventos.menu_bomdia_atrasado()
                opcao = input("Escolha sua ação: ")
                print('-=-'*15)          
                if(opcao == "1"):
                    if(personagem.dinheiro >= 15):
                        personagem.dinheiro -= 15
                        personagem.fome = False
                        time.sleep(0.5)
                        print('Café da manhã na barriga!')
                        print('-=-'*15)
                        relogio.avancaTempo(15)
                    else:
                        time.sleep(0.5)
                        print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
                        print('-=-'*15)  
                        relogio.avancaTempo(5)
                elif(opcao == "2"):
                    if(casa.remedios > 0):
                        casa.remedios -= 1
                        personagem.medicado = True
                        time.sleep(0.5)
                        print('Remédio tomado!')
                        print('-=-'*15) 
                        relogio.avancaTempo(5) 
                    else:
                        time.sleep(0.5)
                        print("Não tem remédio na sua casa.")
                        relogio.avancaTempo(5)
                elif(opcao == "3"):           
                    time.sleep(0.5)     
                    print("Você foi trabalhar.")                
                    print('-=-'*15)
                    relogio.avancaTempo(10)
                    recebido = personagem.salario
                    if(not personagem.medicado):
                        time.sleep(0.5)
                        print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho.")
                        recebido = 0
                        personagem.advertencia += 2
                        if casa.remedios > 0:
                            time.sleep(0.5)
                            print("\nVocê chega em casa triste, toma seu remédio e vai dormir!")
                            casa.remedios -= 1
                        else:
                            time.sleep(0.5)
                            print("\nVocê chega em casa para descansar e percebe que não tem remédio para tomar, você tá ferrado!")
                            personagem.HP -= 2
                    elif(personagem.sujo):
                        time.sleep(0.5)
                        print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência. Você volta para casa cabisbaixo e não consegue tomar um banho.")
                        recebido *= 0.9
                        personagem.advertencia += 1
                    elif(personagem.fome):
                        time.sleep(0.5)
                        print("Como você estava com fome, você trabalhou metade do que consegue trabalhar. Sendo assim você volta para casa faminto e come a primeira coisa que vê pela frente.")
                        recebido *= 0.5
                        if casa.comida > 0:
                            time.sleep(0.5)
                            print("\nVocê chega em casa triste, come sua comida e vai dormir!")
                            casa.comida -= 1
                        else:
                            time.sleep(0.5)
                            print("\nVocê chega em casa para descansar e percebe que não tem comida para comer, você tá ferrado!")
                            personagem.HP -= 2
                    elif(relogio.atrasado()):
                        time.sleep(0.5)
                        print("Como você chegou atrasado, você produziu menos do que de costume e recebeu uma advertencia.")
                        recebido *= 0.8
                        personagem.advertencia += 1
                    time.sleep(0.5)
                    print("Você recebeu "+str(recebido)+" reais pelo seu trabalho hoje.")
                    print('-=-'*15)
                    personagem.dinheiro += recebido
                    time.sleep(0.5)
                    print('------ DIA ENCERRADO! ------')
                    time.sleep(0.5)
                    personagem.dormir()
                    relogio = RelogioModulo.Relogio()
                    dia+=1
                elif(opcao == '4'):                    
                    print(f'***** SITUAÇÃO ATUAL: *****\n{personagem}')                    
                elif(opcao == '5'):
                    if(personagem.dinheiro >= 20):
                        casa.remedios += 10
                        personagem.dinheiro -= 20
                        relogio.avancaTempo(10)
                        time.sleep(0.5)
                        print("Comprada a cartela com 10 remédios.")
                        print('-=-'*15)                        
                    else:
                        time.sleep(0.5)
                        print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                        relogio.avancaTempo(5)
                elif(opcao == "0"):
                    break
            else:
                print('-=-'*15)        
                print(str(personagem.nome)+" são "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até as 07:00 então cuidado para não atrasar.")
                eventos.menu_bomdia_seguro()
                opcao = input("Escolha sua ação: ")
                print('-=-'*15)
                if(opcao == "1"):
                    if(casa.comida > 0):
                        casa.comida -= 1
                        personagem.fome = False
                        time.sleep(0.5)
                        print('Café da manhã na barriga!')
                        print('-=-'*15)
                        relogio.avancaTempo(15)
                    else:
                        time.sleep(0.5)
                        print("Não há comida em casa.")
                        relogio.avancaTempo(5)
                elif(opcao == "2"):
                    if(casa.remedios > 0):
                        casa.remedios -= 1
                        personagem.medicado = True
                        time.sleep(0.5)
                        print('Remédio tomado!')
                        print('-=-'*15)  
                        relogio.avancaTempo(5)
                    else:
                        time.sleep(0.5)
                        print("Não tem remédio na sua casa.")
                        relogio.avancaTempo(5)
                elif(opcao == "3"):
                    personagem.sujo = False
                    relogio.avancaTempo(20)
                    time.sleep(0.5)
                    print('Banho tomado!')
                    print('-=-'*15)
                elif(opcao == "4"):
                    time.sleep(0.5)                
                    print("Você foi trabalhar.")                
                    print('-=-'*15)
                    relogio.avancaTempo(10)
                    if relogio.horas >= 7:
                        personagem.atrasado = True
                    recebido = personagem.salario
                    if(not personagem.medicado):
                        time.sleep(0.5)
                        print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho. Sendo assim seu chefe lhe aplica 2 advertências.")
                        recebido = 0
                        personagem.advertencia += 2
                        if casa.remedios > 0:
                            time.sleep(0.5)
                            print("\nVocê chega em casa triste, toma seu remédio e vai dormir!")
                            casa.remedios -= 1
                        else:
                            time.sleep(0.5)
                            print("\nVocê chega em casa para descansar e percebe que não tem remédio para tomar, você tá ferrado!")
                            personagem.HP -= 2
                    elif(personagem.sujo):
                        time.sleep(0.5)
                        print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência. Você volta para casa cabisbaixo e não consegue tomar um banho.")
                        recebido *= 0.9
                        personagem.advertencia += 1
                    elif(personagem.fome):
                        time.sleep(0.5)
                        print("Como você estava com fome, você trabalhou metade do que consegue trabalhar. Sendo assim você volta para casa faminto e come a primeira coisa que vê pela frente.")
                        recebido *= 0.5
                        if casa.comida > 0:
                            time.sleep(0.5)
                            print("\nVocê chega em casa triste, come sua comida e vai dormir!")
                            casa.comida -= 1
                        else:
                            time.sleep(0.5)
                            print("\nVocê chega em casa para descansar e percebe que não tem comida para comer, você tá ferrado!")
                            personagem.HP -= 2
                    elif(personagem.atrasado):
                        time.sleep(0.5)
                        print("Como você chegou atrasado, você produziu menos do que de costume e levou uma advertência.")
                        recebido *= 0.8
                        personagem.advertencia += 1
                    else:
                        time.sleep(0.5)
                        print("Você chegou bem ao trabalho e conseguiu trabalhar bem, seu chefe gostou da atitude e te elogiou!")
                        personagem.elogio += 1
                    print("Você recebeu "+str(recebido)+" reais pelo seu trabalho hoje.")
                    print('-=-'*15)
                    personagem.dinheiro += recebido
                    time.sleep(0.5)
                    print('------ DIA ENCERRADO! ------')
                    time.sleep(0.5)
                    personagem.dormir()
                    relogio = RelogioModulo.Relogio()
                    dia+=1
                elif(opcao == '5'):
                    time.sleep(0.5)
                    print(f'***** SITUAÇÃO ATUAL: *****\n{personagem}')
                elif(opcao == '6'):
                    if(personagem.dinheiro >= 20):
                        casa.remedios += 10
                        personagem.dinheiro -= 20
                        relogio.avancaTempo(10)
                        time.sleep(0.5)
                        print("Comprada a cartela com 10 remédios.")
                        print('-=-'*15)
                    else:
                        time.sleep(0.5)
                        print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                        print('-=-'*15)
                        relogio.avancaTempo(5)
                elif(opcao == '7'):
                    if(personagem.dinheiro >= 30):
                        casa.comida += 5
                        personagem.dinheiro -= 30
                        relogio.avancaTempo(20)
                        time.sleep(0.5)
                        print("Feira feita, adicionado 5 comidas no estoque.")
                        print('-=-'*15)
                    else:
                        time.sleep(0.5)
                        print("5 comidas custam 30 reais, você não tem dinheiro suficiente.")
                        print('-=-'*15)
                        relogio.avancaTempo(5)
                elif(opcao == "0"):
                    break
                else:
                    time.sleep(0.5)
                    print("Opção inválida!")
                    relogio.avancaTempo(5)
        elif personagem.demitido == True:
            print(str(personagem.nome)+" são "+str(relogio)+" do dia "+str(dia)+". Você não tem mais um emprego, vá atrás de um.\n")
            eventos.menu_bomdia_desempregado()
            opcao = input("Escolha sua ação: ")
            print('-=-'*15)
            if(opcao == "1"):
                if(casa.comida > 0):
                    casa.comida -= 1
                    personagem.fome = False
                    time.sleep(0.5)
                    print('Café da manhã na barriga!')
                    print('-=-'*15)
                    relogio.avancaTempo(15)
                else:
                    time.sleep(0.5)
                    print("Não há comida em casa.")
                    relogio.avancaTempo(5)
            elif(opcao == "2"):
                if(casa.remedios > 0):
                    casa.remedios -= 1
                    personagem.medicado = True
                    time.sleep(0.5)
                    print('Remédio tomado!')
                    print('-=-'*15)  
                    relogio.avancaTempo(5)
                else:
                    time.sleep(0.5)
                    print("Não tem remédio na sua casa.")
                    relogio.avancaTempo(5)
            elif(opcao == "3"):
                personagem.sujo = False
                relogio.avancaTempo(20)
                time.sleep(0.5)
                print('Banho tomado!')
                print('-=-'*15)
            elif(opcao == "4"):                
                chance = random.randint(1,20)
                if chance <= 5:
                    relogio.avancaTempo(5)
                    time.sleep(0.5)
                    chance_emprego = input("Te chamaram para uma entrevista na academia do bairro, você aceita? [S][N]")
                    if chance_emprego.upper() == "S":
                        if personagem.peso.upper() == "GORDO":
                            time.sleep(0.5)
                            print("Infelizmente você é gordo e não atende às expectativas de estética dessa maldita empresa!")
                            print('-=-'*15)
                        else:
                            if personagem.altura < 1.79:
                                time.sleep(0.5)
                                print("Você é baixo e não atende às expectativas de estética dessa maldita empresa!")
                                print('-=-'*15)
                            else:
                                time.sleep(0.5)
                                escolha_final = input("Você atende aos requisitos da vaga, o salário é de R$80 por dia, aceita? [S][N]")
                                if escolha_final.upper() == "S":
                                    time.sleep(0.5)
                                    print("Parabéns, você está contratado!")
                                    print('-=-'*15)
                                    personagem.demitido = False
                                    personagem.salario = 80
                                elif escolha_final.upper() == "N":
                                    time.sleep(0.5)
                                    print("Vai catar coquinho então!")
                                    print('-=-'*15)
                                else:
                                    time.sleep(0.5)
                                    print("Digitou errado, parabéns por perder mais um dia!")
                                    print('-=-'*15)
                    elif chance_emprego.upper() == "N":
                        time.sleep(0.5)
                        print("Vai catar coquinho então!")
                        print('-=-'*15)
                    else:
                        time.sleep(0.5)
                        print("Valor digitado inválido, parabéns por perder mais 1 dia.")
                        print('-=-'*15)
                elif chance == 6:
                    time.sleep(0.5)
                    print("Você foi atropelado e morreu no caminho, tente novamente!")
                    sys.exit()
                elif chance <= 10:
                    time.sleep(0.5)
                    chance_emprego = input("Você foi chamado para trabalhar em um salão de cabelo, gostaria de ir? [S][N]")
                    if chance_emprego.upper() == "S":
                        if personagem.cabelo.upper() == "CARECA":
                            time.sleep(0.5)
                            print("Puts, tu é careca, vai dar um exemplo ruim pros nossos clientes!")
                        else:
                            time.sleep(0.5)
                            escolha_final = input("Você atende aos requisitos da vaga, o salário é de R$60 por dia, aceita? [S][N]")
                            if escolha_final.upper() == "S":
                                time.sleep(0.5)
                                print("Parabéns, você está contratado!")
                                print('-=-'*15)
                                personagem.demitido = False
                                personagem.salario = 60
                            elif escolha_final.upper() == "N":
                                time.sleep(0.5)
                                print("Vai catar coquinho então!")
                                print('-=-'*15)
                            else:
                                time.sleep(0.5)
                                print("Digitou errado, parabéns por perder mais um dia!")
                                print('-=-'*15)
                    elif chance_emprego.upper() == "N":
                        time.sleep(0.5)
                        print("Vai catar coquinho então!")
                        print('-=-'*15)
                    else:
                        time.sleep(0.5)
                        print("Valor digitado inválido, parabéns por perder mais 1 dia.")
                        print('-=-'*15)
                elif chance <= 15:
                    time.sleep(0.5)
                    chance_emprego = input("Você foi chamado para trabalhar em uma balada alternativa, gostaria de ir? [S][N]")
                    if chance_emprego.upper() == "S":
                        if personagem.genero.upper() == "MULHER":
                            time.sleep(0.5)
                            escolha_final = input("A vaga é para stripper, R$120 por noite, aceita? [S][N]")
                            if escolha_final.upper() == "S":
                                time.sleep(0.5)
                                print("Parabéns, você está contratado!")
                                print('-=-'*15)
                                personagem.demitido = False
                                personagem.salario = 120
                            elif escolha_final.upper() == "N":
                                time.sleep(0.5)
                                print("Vai catar coquinho então!")
                                print('-=-'*15)
                            else:
                                time.sleep(0.5)
                                print("Digitou errado, parabéns por perder mais um dia!")
                                print('-=-'*15)
                        elif personagem.genero.upper() == "HOMEM":
                            time.sleep(0.5)
                            escolha_final = input("A vaga é para barman, R$90 por noite, aceita? [S][N]")
                            if escolha_final.upper() == "S":
                                time.sleep(0.5)
                                print("Parabéns, você está contratado!")
                                print('-=-'*15)
                                personagem.demitido = False
                                personagem.salario = 90
                            elif escolha_final.upper() == "N":
                                time.sleep(0.5)
                                print("Vai catar coquinho então!")
                                print('-=-'*15)
                            else:
                                time.sleep(0.5)
                                print("Digitou errado, parabéns por perder mais um dia!")
                                print('-=-'*15)
                        elif personagem.genero.upper() == "OUTRO":
                            time.sleep(0.5)
                            escolha_final = input("Hmmm, você é muito mais interessante do que eu imaginava, aceita gerenciar a balada comigo? O salário é de R$200, aceita? [S][N]")
                            if escolha_final.upper() == "S":
                                time.sleep(0.5)
                                print("Parabéns, você está contratado!")
                                print('-=-'*15)
                                personagem.demitido = False
                                personagem.salario = 200
                            elif escolha_final.upper() == "N":
                                time.sleep(0.5)
                                print("Vai catar coquinho então!")
                                print('-=-'*15)
                            else:
                                time.sleep(0.5)
                                print("Digitou errado, parabéns por perder mais um dia!")
                                print('-=-'*15)
                    elif chance_emprego.upper() == "N":
                        time.sleep(0.5)
                        print("Vai catar coquinho então!")
                        print('-=-'*15)
                    else:
                        time.sleep(0.5)
                        print("Valor digitado inválido, parabéns por perder mais 1 dia.")
                        print('-=-'*15)
                elif chance <= 20:
                    time.sleep(0.5)
                    chance_emprego = input("Você foi chamado para trabalhar em uma central de apostas clandestinas e pirâmide finaceira, gostaria de ir? [S][N]")
                    if chance_emprego.upper() == "S":
                        time.sleep(0.5)
                        escolha_final = input("A vaga é para ministrar o JOGO DO BICHO, VENDER INGRESSO FALSO NA RUA e VENDER CURSO DE DAY TRADE, R$250 por dia, aceita? [S][N]")
                        if escolha_final.upper() == "S":
                            time.sleep(0.5)
                            print("Parabéns, você está contratado!")
                            print('-=-'*15)
                            personagem.demitido = False
                            personagem.salario = 250
                            chance_preso = random.randint(1,10)
                            if chance_preso <= 7:
                                time.sleep(0.5)
                                print("Você foi pego fazendo coisa de trambiqueiro e foi preso, não existe dinheiro fácil nessa vida, tente novamente!")
                                sys.exit()
                        elif escolha_final.upper() == "N":
                            time.sleep(0.5)
                            print("Vai catar coquinho então!")
                            print('-=-'*15)
                        else:
                            time.sleep(0.5)
                            print("Digitou errado, parabéns por perder mais um dia!")
                            print('-=-'*15)
                time.sleep(0.5)
                print('------ DIA ENCERRADO! ------')
                time.sleep(0.5)
                personagem.dormir()
                relogio = RelogioModulo.Relogio()
                dia+=1
            elif(opcao == '5'):
                time.sleep(0.5)                
                print(f'***** SITUAÇÃO ATUAL: *****\n{personagem}')                
            elif(opcao == '6'):
                if(personagem.dinheiro >= 20):
                    casa.remedios += 10
                    personagem.dinheiro -= 20
                    relogio.avancaTempo(10)
                    time.sleep(0.5)
                    print("Comprada a cartela com 10 remédios.")
                    print('-=-'*15)
                else:
                    time.sleep(0.5)
                    print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                    print('-=-'*15)
                    relogio.avancaTempo(5)
            elif(opcao == '7'):
                if(personagem.dinheiro >= 30):
                    casa.comida += 5
                    personagem.dinheiro -= 30
                    relogio.avancaTempo(20)
                    time.sleep(0.5)
                    print("Feira feita, adicionado 5 comidas no estoque.")
                    print('-=-'*15)
                else:
                    time.sleep(0.5)
                    print("5 comidas custam 30 reais, você não tem dinheiro suficiente.")
                    print('-=-'*15)
                    relogio.avancaTempo(5)
            elif(opcao == "0"):
                break
            else:
                time.sleep(0.5)
                print("Opção inválida!")
                relogio.avancaTempo(5)