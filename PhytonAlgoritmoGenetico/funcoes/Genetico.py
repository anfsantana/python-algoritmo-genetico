from Gene import Gene
from Cromossomo import Cromossomo
from Candidato import Candidato
class Genetico:

    @staticmethod    
    def gerarPopulacao(totalIndividuos, totalGene ):  
        tempListaGene = list()
        tempListaCromossomo = list()
        candidatos = Candidato()
        try:
            for x in range(0, totalIndividuos):
                cromossomo = Cromossomo()
                for g in range(0, totalGene): #Ver regra para quantidade de genes.
                    gene = Gene()   
                    tempListaGene.append(gene)
                cromossomo.listaGene = tempListaGene
                tempListaGene = list()
                tempListaCromossomo.append(cromossomo)
            candidatos.listaCandidatos = tempListaCromossomo
        except Exception as ex:
            print("Ocorreu o erro: {0} ".format(ex.args))
        finally:
            tempListaGene = list()
            tempListaCromossomo = list()                  
        return candidatos

    @staticmethod    
    def listarCandidatos(populacao):
        print("\n")  
        try:
            for candidato in populacao:    
                for gene in candidato.listaGene:            
                    print ("%d" % gene.informacao, end="", flush=True)
                print("\n")
        except Exception as ex:
            print("Ocorreu o erro: {0} ".format(ex.args))

    #@staticmethod    
    #def aplicarCruzamento(populacao):
    #    print("\n")  
    #    try:
    #        for candidato in populacao:    
    #            for gene in candidato.listaGene:            
    #                print ("%d" % gene.informacao, end="", flush=True)
    #            print("\n")
    #    except Exception as ex:
    #        print("Ocorreu o erro: {0} ".format(ex.args))

    @staticmethod    
    def avaliar(populacao):
        sum = 0
        try:
            for candidato in populacao:    
                for gene in candidato.listaGene:            
                    sum = sum + gene.informacao   
                candidato.avaliacao = sum
                sum = 0            
        except Exception as ex:
            print("Ocorreu o erro: {0} ".format(ex.args))

    #@staticmethod    
    #def aplicarCondicao(populacao, valorEsperado, quantidadeIndividuos):
    #    sum = 0
    #    try:
    #        for candidato in populacao:    
    #            for gene in candidato.listaGene:            
    #                sum = sum + gene.informacao   
    #            candidato.setAvaliacao(sum)
    #            sum = 0            
    #    except Exception as ex:
    #        print("Ocorreu o erro: {0} ".format(ex.args))