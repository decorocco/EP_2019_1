# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:50:54 2019

@author: Aspire_andre
"""
#Funções utilizadas no game
def pergunta():
    perg=input("O que deseja fazer, \033[35m{}\033[m? >>".format(nome_jogador)).strip
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


#game pilot EP1
import time
import random
inventario = []
print("Você se encontra no meio do saguão de sua universidade, o Insper.")
nome_jogador = input("Qual o seu nome, honorável sofredor universitário? >>")
time.sleep(1)
print()
print("Você se lembra que está atrasado na entrega de seu EP de Design de software, mas você não está a fim de termina-lo.")
print("Você vê seus amigos que já terminaram o projeto saindo para ir ao cinema assistir Guerra Finita:Começato.")
print("Você também pode ignora-los e ir à biblioteca.\n\nIr à biblioteca = biblioteca \nIr com seus amigos ao cinema = cinema") 

def escolha1():
    resposta1 = pergunta()
    while resposta1 != ("biblioteca") and resposta1 != ("cinema"):
        print("Resposta inválida!")
        resposta1 = pergunta()
    if resposta1 == "biblioteca":
        #funcao biblioteca
        print("Você se dirige à biblioteca")
    elif resposta1 == "cinema":
        #funcao cinema
        print("você alcança seus amigos e parte para o cinema")
    return resposta1
    
escolha1()
