from Gene import Gene
from Cromossomo import Cromossomo
from Candidato import Candidato


#Simulando testando preenchimento e listagem

candidato = Candidato([])

for x in range(0, 4):
    cromossomo = Cromossomo([])
    for g in range(0, 4):
        gene = Gene()   
        cromossomo.listaGene.append(gene)
    candidato.listaCandidatos.append(cromossomo)

for cand in candidato.listaCandidatos:
    for gene in cand.listaGene:
        print ("%d" % gene.informacao, end="", flush=True)
    print("\n")
