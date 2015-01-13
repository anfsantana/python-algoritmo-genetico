from Gene import Gene
from Cromossomo import Cromossomo
from Candidato import Candidato
class Genetico:

    @staticmethod    
    def gerarCandidatos(quantidadeCandidatos):  
        quantidadeCandidatos = quantidadeCandidatos-1
        candidatos = Candidato(list())
        for x in range(0, quantidadeCandidatos):
            cromossomo = Cromossomo(list())
            for g in range(0, quantidadeCandidatos): #Ver regra para quantidade de genes.
                gene = Gene()   
                cromossomo.listaGene.append(gene)
            candidatos.listaCandidatos.append(cromossomo)
        return  candidatos

    @staticmethod    
    def listarCandidatos(listaCandidatos):
        print("\n")  
        try:
            for candidato in listaCandidatos:    
                for gene in candidato.listaGene:            
                    print ("%d" % gene.informacao, end="", flush=True)
                print("\n")
        except Exception as ex:
            print("Ocorreu o erro: {0} ".format(ex.args))
