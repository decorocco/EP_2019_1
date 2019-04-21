# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:50:54 2019

@author: Aspire_andre
"""
#features
inventario = []
locais_visitados = []
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
    inventario.append("pen-drive")
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
    print("Após pensar um pouco, voce realiza ter duas opções:\n\nIr para a biblioteca = biblioteca \nIr para o quarto andar do prédio 1 jogar smash = smash" )
def funusar():
    print("Voce decide tentar usar a máquina de teletransporte")
    time.sleep(2)
    print("Ao chegar mais perto do painel da máquina, é possível ler a seguinte menssagem no monitor:")
    print("Insira o nome do local para qual voce deseja se teletransportar:") 
def funsmash():
    print("Ao chegar no quarto andar, voce se depara com alguns veteranos jogando smash no wii que existe no meio da sala")
    print("Um dos veteranos te afronta, pois não gosta da sua presença no local e te chama para uma luta")
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
    print("Você vê de longe 2 figuras distorcidas, que se aproximam aos poucos de onde voce está")	
    print("Agora que estão em sua frente, voce reconhece as duas figuras que estão emanando a aura intensa que voce tinha sentido...")	
    time.sleep(2)	
    print("Você encontra \033[36mBill Gates\033[m!")	
    time.sleep(1)	
    print("\033[36mBill Gates\033[m:Oi \033[35m{}\033[m, por que você está tão aflito com a EP de programação?".format(nome_jogador))	
    time.sleep(2)	
    print("\033[36mBill Gates\033[m:Não precisa se preocupar tanto com essas coisas")	
    time.sleep(2)	
    print("\033[36mBill Gates\033[m:Acredite em mim, é nos momentos de ócio que se tem as melhores ideias!")	
    time.sleep(2)	
    print("\033[36mBill Gates\033[m:Por isso consegui criar a Microsoft, a procastinação é a chave do sucesso \033[35m{}\033[m!")	
    inventario.append("Benção do Bill Gates")	
    print("\033[32mBenção do Bill Gates adicionada ao inventário!\033[m")
    
    
#game pilot EP1
import time
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
    if "biblioteca" not in locais_visitados:
        locais_visitados.append("biblioteca")
    funbiblioteca()
    resposta2 = pergunta()
    while resposta2 != "mentira" and resposta2 != "verdade":
        print("Resposta Inválida!")
        resposta2 = pergunta()
    if resposta2 == "mentira":
        funmentira()
    elif resposta2 == "verdade":
        funverdade()
    funbiblioteca2()
elif resposta1 == "cinema":
    if "cinema" not in locais_visitados:
        locais_visitados.append("cinema")
    funcinema()
    resposta3 = pergunta()
    while resposta3 != "biblioteca" and resposta3 != "filme":
        print('Resposta Inválida!')
        resposta3 = pergunta()
    if resposta3 == "biblioteca":
        funbiblioteca()
    elif resposta3 == "filme":
        funfilme()
        resposta4 = pergunta()
        while resposta4 != "insper" and resposta4 != "esperar":
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
                resposta5b = pergunta()
                while resposta5b != "biblioteca" and resposta5b != "smash":
                    print("Resposta Inválida")
                    resposta5b = pergunta()
                if resposta5b == "biblioteca":
                    funbiblioteca()
                elif resposta5b == "smash":
                    funsmash()
            elif resposta5 == "usar":
                funusar()
                print("Estes são os lugares para quais você pode teleportar: {}".format(locais_visitados))
                respostatp = perguntatp()
                while respostatp not in locais_visitados:
                    print("Local não reconhecido")
                    respostatp = perguntatp()
                if respostatp == "biblioteca":
                    funbiblioteca()
                elif respostatp == "cinema":
                    funcinema()
        elif resposta4 == "insper":
            funinsper()
            resposta6 = pergunta()
            while resposta6 != "biblioteca" and resposta6 != "smash" and resposta6 != "atestado":
                print("Resposta Inválida")
                resposta6 = pergunta()
            if resposta6 == "biblioteca":
                funbiblioteca()
            elif resposta6 == "smash":
                funsmash()
        elif resposta4 == "atestado":
            funhospital()
            
    
    
