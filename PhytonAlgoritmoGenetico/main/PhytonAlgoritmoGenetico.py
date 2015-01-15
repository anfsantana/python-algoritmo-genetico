# -*- coding: cp1252 -*- 
from Genetico import Genetico
from Cromossomo import Cromossomo
from Gene import Gene
import time
import os

funcGenetico = Genetico()
totalGene = 7
#Ver questÃµes dos acentos
print(" SUGESTÃO DE COMPETÊNCIAS \n PARA O CARGO DE [Coordenador de Recursos Humanos]")

totalIndividuos = input("\n 1. Insira a quantidade de candidatos para serem gerados aleatóriamente: ")
valorEsperado =   input("\n 2. Insira o valor mínimo para a seleção de candidatos: ")
quantidadeIndividuos = input("\n 3. Insira a quantidade máxima de candidatos que se deseja obter: ")

os.system("cls")

print("\n ===================== CONFIGURAÇÕES DO PROGRAMA ===================== ")
print("\n Total de candidatos: {0} ".format(totalIndividuos))
print("\n Valor mínimo para a seleção de candidatos: {0} ".format(valorEsperado))
print("\n Quantidade mínima de candidatos que se deseja obter : {0}".format(quantidadeIndividuos))
print("\n [Padrão/Programa] Total de critérios de avaliação : {0} ".format(totalGene));
print("\n ===================================================================== ")

print (" \n\n Gerando candidatos ... \n\n")
time.sleep(5)
candidatos = Genetico().gerarPopulacao(int(totalIndividuos), int(totalGene))
Genetico().listarCandidatos(candidatos.listaCandidatos)

print (" \n\n Avaliando candidatos ... \n\n")
time.sleep(5)
Genetico().avaliar(candidatos.listaCandidatos)

#Descomentar e continuar fazendo ... Senão fica em loop infinito.
#while (Genetico().aplicarCondicao(candidatos.listaCandidatos, int(valorEsperado), int(quantidadeIndividuos))):
#       Genetico().selecionar(candidatos.listaCandidatos, int(totalIndividuos), int(totalGene), int(quantidadeIndividuos)) 
