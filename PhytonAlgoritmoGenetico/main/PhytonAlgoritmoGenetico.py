from Genetico import Genetico
from Cromossomo import Cromossomo
from Gene import Gene
funcGenetico = Genetico()

quantCandidatos = input("Digite a quantidade de candidatos para serem gerados: ")

candidatos = funcGenetico.gerarCandidatos(int(quantCandidatos))
funcGenetico.listarCandidatos(candidatos.listaCandidatos)