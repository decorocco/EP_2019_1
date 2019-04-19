# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:50:54 2019

@author: Aspire_andre
"""

#game pilot EP1
import time
import random as rd
inventario = []
print("Você se encontra no meio do saguão de sua universidade, o Insper.")
nome_jogador = input("Qual o seu nome, honorável sofredor universitário? >>")
time.sleep(1)
print()
print("Você se lembra que está atrasado na entrega de seu EP de Design de software, mas você não está a fim de termina-lo.")
print("Você vê seus amigos que já terminaram o projeto saindo para ir ao cinema assistir Guerra Finita:Começato.")
print("Você também pode ignora-los e ir à biblioteca.\n\nIr à biblioteca = biblioteca \nIr com seus amigos ao cinema = cinema") 

def escolha1():
    resposta1 = input("O que deseja fazer, {}? >>".format(nome_jogador)).strip
    while resposta1 != ("biblioteca") and resposta1 != ("cinema"):
        print("Resposta inválida!")
        resposta1 = input("O que deseja fazer, {}? >>".format(nome_jogador)).strip
    if resposta1 == "biblioteca":
        #funcao biblioteca
        print("Você se dirige à biblioteca")
    elif resposta1 == "cinema":
        #funcao cinema
        print("você alcança seus amigos e parte para o cinema")
    return resposta1
    
escolha1()
