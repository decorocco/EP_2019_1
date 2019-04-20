# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:50:54 2019

@author: Aspire_andre
"""
inventario = []
#Funções utilizadas no game
def pergunta():
    perg=input("O que deseja fazer, \033[35m{}\033[m? >>".format(nome_jogador)).strip().lower()
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
    print('\033[36mToshi\033[m:Voce não devia ter procastinado para fazer está EP.')
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
    print("Pen-drive adicionado ao inventário")
def funfilme():
    print('\033[36mBárbara\033[m se despede, e voce entra na sessão do filme com seus amigos')
    time.sleep(4)
    print('Após 3 horas de filme, seus olhos estão sangrando de tão bom que ele consegue ser!')
    time.sleep(1)
    print('Um de seus amigos sugere que voces saiam da sala e voltem para o Insper\n\nVoltar para o Insper = insper \nEsperar os créditos = esperar')
def funesperar():
    print('Voces esperam as cenas pós-créditos como em todos os filmes da Marvel')
    print('Quando estão saindo da sala de cinema, voce nota algo estranho atrás da tela de cinema...')
    time.sleep(2)
    print('Após decidir verificar, voce descobre uma sala secreta atrás da tela!')
    print('É uma sala com uma máquina enorme e estranha em seu interior, com muitos cabos elétricos e tomadas')
    time.sleep(2)
    print('Uma \033[31mSala de Teletransporte\033[m!')
    time.sleep(2)
    print('Voce encontra o manual da máquina e descobre que para utiliza-la, deve saber exatamente o nome do local que deseja ir!\n\nUsar a máquina = usar \nIgnorar e voltar ao Insper com seus amigos = insper')
    
#game pilot EP1
import time
import random
print("Você se encontra no meio do saguão de sua universidade, o Insper.")
nome_jogador = input("Qual o seu nome, honorável sofredor universitário? >>")
time.sleep(1)
print()
print("Você se lembra que está atrasado na entrega de seu EP de Design de software, mas você não está a fim de termina-lo.")
print("Você vê seus amigos que já terminaram o projeto saindo para ir ao cinema assistir Guerra Finita:Começato.")
print("Você também pode ignora-los e ir à biblioteca.\n\nIr à biblioteca = biblioteca \nIr com seus amigos ao cinema = cinema") 


    
resposta1 = pergunta()
print(resposta1)
while resposta1 != "biblioteca" and resposta1 != "cinema":
    print("Resposta Inválida!")
    resposta1 == pergunta()
if resposta1 == "biblioteca":
    funbiblioteca()
    resposta2 = pergunta()
    while resposta2 != "mentira" and resposta2 != "verdade":
        print("Resposta Inválida!")
        resposta2 = pergunta()
    if resposta2 == "mentira":
        funmentira()
    elif resposta2 == "verdade":
        funverdade()
elif resposta1 == "cinema":
    funcinema()
    
