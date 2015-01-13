from Gene import Gene
from Cromossomo import Cromossomo
from Candidato import Candidato
class Genetico:

    @staticmethod    
    def gerarCandidatos():  
        candidatos = Candidato(list())
        for x in range(0, 4):
            cromossomo = Cromossomo(list())
            for g in range(0, 4):
                gene = Gene()   
                cromossomo.listaGene.append(gene)
            candidatos.listaCandidatos.append(cromossomo)
        return  candidatos

    @staticmethod    
    def listarCandidatos():  
        try:
            for candidato in Genetico.gerarCandidatos().listaCandidatos:    
                for gene in candidato.listaGene:            
                    print ("%d" % gene.informacao, end="", flush=True)
                print("\n")
        except Exception as ex:
            print("Ocorreu o erro: {0} ".format(ex.args))
