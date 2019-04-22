# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:50:54 2019

@author: Aspire_andre
"""
#Bibliotecas
import random
import time

#features
inventario = []
locais_visitados = []
toshi_hp = 30
player_hp = 15
possiveis_ataques = []
acertar_ataque=random.randint(0, 10)
acaso_encontro=random.randint(0,1)

#Funções utilizadas no game
def pergunta():
    perg=input("O que deseja fazer, \033[35m{}\033[m? >>".format(nome_jogador)).strip().lower()
    return perg
def perguntatp():
    perg=input("Para onde deseja teleportar, \033[35m{}\033[m? >>".format(nome_jogador)).strip().lower()
    return perg
def funcinema():
    print('Voce alcança seus amigos e parte para o cinema')
    print('Ao chegar no shopping com seus amigos, voces se dirigem à bilheteria para comprar seus ingressos')
    print('Porém, ao entrar na fila, voce se depara com a \033[36mBárbara\033[m')
    time.sleep(2)
    print('\033[36mBárbara\033[m:Ola \033[35m{}\033[m, tudo bem?'.format(nome_jogador))
    time.sleep(2)
    print('\033[36mBárbara\033[m:Ainda não recebemos a sua EP1 no BlackBoard, ainda bem que te encontrei aqui!')
    time.sleep(2)
    print('\033[36mBárbara\033[m:Voce não acha melhor entrega-la ao invés de ver o filme?\n\nVoltar à biblioteca = biblioteca \nEntrar na sessão do filme = filme')
def funbiblioteca():
    print('Você parte em direção à biblioteca do Insper')
    print('Na entrada da biblioteca você sente um distúrbio na força. Uma aura imensa se revela!')
    print('Você pensa: Que imenso poder de computação!!! É evidente, a única pessoa capaz de emanar algo assim é o...')
    print('Você se depara com \033[36mToshi\033[m, seu professor de programação.')
    time.sleep(2)
    print('\033[36mToshi\033[m:Oi \033[35m{}\033[m! Tudo bem?'.format(nome_jogador))
    time.sleep(2)
    print('\033[36mToshi\033[m:Como vai a confecção da EP1?\n\nEstá indo muito bem, vou tirar um 10! = mentira \nEntão professor...eu não fiz nada ainda, posso entregar outro dia? = verdade')
def funmentira():
    print('\033[36mToshi\033[m:Que bom!')
    time.sleep(2)
    print('\033[36mToshi\033[m:Espero então que sua EP1 esteja fantástica \033[35m{}\033[m!'.format(nome_jogador))
    time.sleep(2)
    print('Após a breve conversa, voce vê \033[36mToshi\033[m indo embora e sente que a pressão que estava sendo exercida por sua aura programadora volta ao normal')
    time.sleep(4)
    print('Voce entra na biblioteca...')
def funverdade():
    print('\033[36mToshi\033[m:Hmm....')
    time.sleep(4)
    print('\033[36mToshi\033[m:Infelizmente isso não é possível \033[35m{}\033[m'.format(nome_jogador))
    time.sleep(2)
    print('\033[36mToshi\033[m:Voce não devia ter procastinado para fazer esta EP.')
    time.sleep(2)
    print('\033[36mToshi\033[m:Agora voce vai ter que arcar com as consequências!')
    time.sleep(1)
    print('Voce sente a aura de programação que voce tinha sentido anteriormente se intensificar!')
    print('\033[36mToshi\033[m vai embora e voce tem o sentimento de que o equilibrio do mundo voltou ao normal')
    time.sleep(2)
    print('Após ficar algum tempo parado pensando na frente da biblioteca, voce nota a existência de um pen-drive no chão, onde teve sua conversa com o \033[36mToshi\033[m')
    time.sleep(2)
    print('Voce pega o \033[32mPen-Drive\033[m e entra na biblioteca...')
    inventario.append("Pen-drive")
    print("\033[32mPen-drive adicionado ao inventário!\033[m")
def funfilme():
    print('\033[36mBárbara\033[m se despede, e voce entra na sessão do filme com seus amigos')
    time.sleep(4)
    print('Após 3 horas de filme, seus olhos estão sangrando de tão bom que a experiência foi! Você não vê a hora de assistir a cena pós-créditos')
    time.sleep(1)
    print("É ai que vem uma ideia à sua cabeça. Você poderia tentar adiar a entrega da EP por meio de um atestado médico!")
    print('Um de seus amigos sugere que voces saiam da sala e voltem para o Insper\n\nVoltar para o Insper = insper \nEsperar os créditos = esperar\nIr ao hospital para tentar pegar um atestado = atestado')
def funesperar():
    print('Vocês esperam as cenas pós-créditos como em todos os filmes da Mervel')
    print('Quando estão saindo da sala de cinema, você nota algo estranho atrás da tela de cinema...')
    time.sleep(2)
    print('Após decidir verificar, você descobre uma sala secreta atrás da tela!')
    print('É uma sala com uma máquina enorme e estranha em seu interior, com muitos cabos elétricos e tomadas')
    time.sleep(2)
    print('Uma \033[31mSala de Teletransporte\033[m!')
    time.sleep(2)
    print('Voce encontra o manual da máquina e descobre que para utiliza-la, deve saber exatamente o nome do local que deseja ir!\n\nUsar a máquina = usar \nIgnorar e voltar ao Insper com seus amigos = insper')
def funinsper():
    print("Voce retornou ao saguão do Insper")
    time.sleep(2)
    print("Após pensar um pouco, você percebe nao ter nada a fazer além de ir à biblioteca.")
    time.sleep(2)
def funusar():
    print("Voce decide tentar usar a máquina de teletransporte")
    time.sleep(2)
    print("Ao chegar mais perto do painel da máquina, é possível ler a seguinte menssagem no monitor:")
    print("Insira o nome do local para qual voce deseja se teletransportar:") 
def funbiblioteca2():
    print()
    print()	
    print("Ao entrar na biblioteca voce acha uma sala de estudos vazia e decide entrar para utiliza-la")	
    print("Você não consegue se concentrar pois a única coisa que vem em sua cabeça é o que seus amigos podem estar fazendo de divertido, e o quanto você não quer fazer a EP.")	
    print("Você se sente estranho por alguns segundos...")	
    time.sleep(3)	
    print("Você passa mal e acaba desmaiando, já que não se alimentou durante o dia, e saiu sem comer de casa para não se atrasar para a aula")	
    time.sleep(2)	
    print("Enquanto vaga por um lugar vazio e desconhecido no qual você se encontra, você novamente sente uma aura programadora muito forte, porém diferente da aura sentida anteriormente...")	
    time.sleep(3)	
    print("Você vê de longe uma figura distorcida, que se aproxima aos poucos de onde voce está")	
    print("Agora que está em sua frente, você reconhece a figura que está emanando a aura intensa que voce tinha sentido...")	
    time.sleep(2)	
    print("Você encontra \033[36mBill Gates\033[m!")	
    time.sleep(1)	
    print("\033[36mBill Gates\033[m:Oi \033[35m{}\033[m, por que você está tão aflito com a EP de programação?".format(nome_jogador))	
    time.sleep(2)	
    print("\033[36mBill Gates\033[m:Não precisa se preocupar tanto com essas coisas")	
    time.sleep(2)	
    print("\033[36mBill Gates\033[m:Acredite em mim, é nos momentos de ócio que se tem as melhores ideias!")	
    time.sleep(2)	
    print("\033[36mBill Gates\033[m:Por isso consegui criar a Microsoft, a procastinação é a chave do sucesso \033[35m{}\033[m!".format(nome_jogador))	
    inventario.append("Benção do Bill Gates")	
    print("\033[32mBenção do Bill Gates adicionada ao inventário!\033[m")
    time.sleep(2)
    print("Voce acorda do seu sonho")
def funbatalha():
    toshi_hp = 30
    player_hp = 15
    if "Pen-drive" in inventario:
        possiveis_ataques.append("Usar Pen drive como chantagem = chantagem")
    if "Benção do Bill Gates" in inventario:
        possiveis_ataques.append("Usar Benção do Bill Gates como exemplo de sucesso = gates")
    print("Você se depara com Toshi e vocês dois sabem que essa batalha é inevitavel para o adiamento da EP")
    if len(inventario) == 2:
        print("Embora a pressão exercida por Toshi é ameaçadora, você se enche de determinação e confiança")
    print("Toshi assume sua pose de batalha e você faz o mesmo")
    time.sleep(3)
    while toshi_hp > 0 and player_hp > 0 and len(possiveis_ataques)>0:
        print("==============================================================================================================================")
        print("Toshi --> HP = {}".format(toshi_hp))
        print("{0} --> HP = {1}".format(nome_jogador,player_hp))
        print("Possíveis ataques:")
        print(possiveis_ataques)
        acao_batalha = pergunta()
        while acao_batalha != "gates" and acao_batalha != "chantagem":
            print("Resposta Inválida")
            acao_batalha = pergunta()
        if acao_batalha == "gates":
            print("\033[35m{}\033[m: Eu falei com o Bill Gates(gatesinho, para os próximos) e ele disse que saiu da faculdade e ainda se deu bem!".format(nome_jogador))
            print("\033[36mToshi\033[m: Ele é um caso à parte!")
            print("Mesmo Toshi estando certo ele leva 15 de dano!")
            print("Você leva 10 de dano!")
            player_hp += -10
            toshi_hp += -15
            possiveis_ataques.remove("Usar Benção do Bill Gates como exemplo de sucesso = gates")
        elif acao_batalha == "chantagem":
            print("\033[35m{}\033[m: Se você não adiar a EP eu vou vazar todas as suas provas futuras!".format(nome_jogador))
            print("Você vê surpresa e desprezo nos olhos de \033[36mToshi\033[m. \033[36mToshi\033[m leva 15 de dano!")
            toshi_hp += -15
            possiveis_ataques.remove("Usar Pen drive como chantagem = chantagem")
    if toshi_hp > 0:
        print("Oh não! Você não tem recursos suficientes para vencer de \033[36mToshi\033[m, o Magnífico")
        print ("GAME OVER")
        print ("FINAL 2/3")
        time.sleep(4)
        print("Muito obrigado por jogar \033[35m{}\033[m!".format(nome_jogador))
    else: 
        print("\033[36mToshi\033[m: C-Como?? Não é possível!!! Parece que vou ter que realmente adiar a entrega. Você venceu, batata frita.")
        print("PARABÉNS, VOCÊ VENCEU")
        print("FINAL 1/3")
        time.sleep(4)
        print("Muito obrigado por jogar \033[35m{}\033[m!".format(nome_jogador))
def funhospital():
    print("Você foi para o hospital mais próximo com muita esperança em seu coração")
    print("Ao chegar lá você encontra um \033[36mMédico\033[m!")
    time.sleep(2)
    print("\033[36mMédico\033[m:Olá, tudo bem?")
    time.sleep(2)
    print("\033[36mMédico\033[m:Nossa, seus olhos estão muito vermelhos!")
    time.sleep(2)
    print("\033[36mMédico\033[m:O senhor por um acaso fez uso de entorpecentes?")
    time.sleep(2)
    print("Você explica para o médico que viu Guerra Finita:Começato")
    time.sleep(2)
    print("\033[36mMédico\033[m:AHHHH, agora faz sentido!")
    time.sleep(2)
    print("\033[36mMédico\033[m:Mas então, o que você precisa?")    
    time.sleep(2)
    print("Você diz precisar de um atestado")
    time.sleep(2)
    print("\033[36mMédico\033[m:Ah, claro! Tome aqui seu atestado!")
    inventario.append("Atestado Médico")
    print("\033[32mAtestado Médico foi adicionado ao inventário!\033[m")
    time.sleep(3)
    print("Parabéns!!!")
    print("Você conseguiu um atestado! Este item faz com que voce possa entregar a EP outro dia!")
    time.sleep(4)
    print("Você ganhou!!!")
    print("FINAL 3/3")
    time.sleep(4)
    print("Muito obrigado por jogar \033[35m{}\033[m!".format(nome_jogador))
def fundescobrir():
    print("Após acordar, você decide checar os contúdos do pen-drive que você encontrou na entrada da biblioteca")
    print("Você se espanta com o que descobre ao mexer nos arquivos que existem dentro do dispositivo")
    time.sleep(2)
    print("Você se espanta ao achar os arquivos das futuras provas de Deisgn de Software!")
    print("É o pen-drive do \033[36mToshi\033[m!")
    time.sleep(2)
    print("Após pensar um pouco, você chega à conclusão de que isto pode ser útil para conseguir adiar a entrega da EP!")
    
def funcontbi():
    if "biblioteca" not in locais_visitados:
        locais_visitados.append("biblioteca")
    funbiblioteca()
    resposta2 = pergunta()
    while resposta2 != "mentira" and resposta2 != "verdade":
        print("Resposta Inválida!")
        resposta2 = pergunta()
    if resposta2 == "mentira":
        funmentira()
        funbiblioteca2()
    elif resposta2 == "verdade":
        funverdade()
        funbiblioteca2()
        fundescobrir()
    funbatalha()
    
def funencontro():
    player_hp = 15
    print("Um veterano selvagem aparece!")
    print("Ele quer sair no soco com você!")
    print("Você pode ataca-lo ou fugir")
    print("Já que bixo nem é gente, seu sucesso na briga é aleatório!\n\nSair no soco com o veterano = ataque \nEnsebar as canelas = fugir")
    decisao = pergunta()
    while decisao != "fugir" and decisao != "ataque":
        print("Resposta Inválida")
        decisao = pergunta()
    if decisao == "fugir":
        print("Você ensebou as canelas e saiu vazado")
    elif decisao == "ataque":
        if acertar_ataque < 4:
            print("Você errou feio, errou rude!")
            print("Você saiu com um olho roxo e com seu orgulho ferido ;-;")
            player_hp += -5
            print("Você levou 5 de dano")
            print("Você está com {} de hp!".format(player_hp))
        else:
            print("Você quem manja mais de Python, chupa vet")
            print("Você ganhou a luta! xD")
            player_hp += 10
            print("Você ganhou 10 hp como bônus por vencer desse bobão!")
            print("Você está com {} de hp!".format(player_hp))
def funacaso():
    if acaso_encontro == 1:
        funencontro()     
    
#game pilot EP1
print("Você se encontra no meio do saguão de sua universidade, o Insper.")
nome_jogador = input("Qual o seu nome, honorável sofredor universitário? >>")
time.sleep(1)
print()
print("Você se lembra que está muito atrasado na entrega de seu EP de Design de software, mas você não está a fim de termina-lo.")
print("Você vê seus amigos que já terminaram o projeto saindo para ir ao cinema assistir Guerra Finita:Começato.")
print("Você pode ignora-los e ir à biblioteca ou segui-los.\n\nIr à biblioteca = biblioteca \nIr com seus amigos ao cinema = cinema") 


    
resposta1 = pergunta()
print(resposta1)
while resposta1 != "biblioteca" and resposta1 != "cinema":
    print("Resposta Inválida!")
    resposta1 = pergunta()
if resposta1 == "biblioteca":
    funacaso()
    time.sleep(3)
    funcontbi()
elif resposta1 == "cinema":
    if "cinema" not in locais_visitados:
        locais_visitados.append("cinema")
    funcinema()
    resposta3 = pergunta()
    while resposta3 != "biblioteca" and resposta3 != "filme":
        print('Resposta Inválida!')
        resposta3 = pergunta()
    if resposta3 == "biblioteca":
        funcontbi()
    elif resposta3 == "filme":
        funfilme()
        resposta4 = pergunta()
        while resposta4 != "insper" and resposta4 != "esperar" and resposta4 != "atestado":
            print("Resposta Inválida!")
            resposta4 = pergunta()
        if resposta4 == "esperar":
            funesperar()
            resposta5 = pergunta()
            while resposta5 != "insper" and resposta5 != "usar":
                print("Resposta Inválida!")
                resposta5 = pergunta()
            if resposta5 == "insper":
                funinsper()
                funcontbi()
            elif resposta5 == "usar":
                funusar()
                print("Estes são os lugares para quais você pode teleportar: {}".format(locais_visitados))
                respostatp = perguntatp()
                while respostatp not in locais_visitados:
                    print("Local não reconhecido")
                    respostatp = perguntatp()
                if respostatp == "biblioteca":
                    funcontbi()
                elif respostatp == "cinema":
                    funcinema()
                    resposta3 = pergunta()
                    while resposta3 != "biblioteca" and resposta3 != "filme":
                        print('Resposta Inválida!')
                        resposta3 = pergunta()
                    if resposta3 == "biblioteca":
                        funcontbi()
                    elif resposta3 == "filme":
                        funfilme()
                        resposta4 = pergunta()
                        while resposta4 != "insper" and resposta4 != "esperar" and resposta4 != "atestado":
                            print("Resposta Inválida!")
                            resposta4 = pergunta()
                        if resposta4 == "esperar":
                            funesperar()
                            resposta5 = pergunta()
                            while resposta5 != "insper" and resposta5 != "usar":
                                print("Resposta Inválida!")
                                resposta5 = pergunta()
                            if resposta5 == "insper":
                                funinsper()
                                funcontbi()
                            elif resposta5 == "usar":
                                funusar()
                                print("Estes são os lugares para quais você pode teleportar: {}".format(locais_visitados))
                                respostatp = perguntatp()
                                while respostatp not in locais_visitados:
                                    print("Local não reconhecido")
                                    respostatp = perguntatp()
                                if respostatp == "biblioteca":
                                    funcontbi()
                                elif respostatp == "cinema":
                                    print("Você não pode fazer isso duas vezes")
                                    print("Você decide voltar à biblioteca")
                                    funcontbi()
        elif resposta4 == "insper":
            funinsper()
            funcontbi()
        elif resposta4 == "atestado":
            funhospital()
            
    
    
