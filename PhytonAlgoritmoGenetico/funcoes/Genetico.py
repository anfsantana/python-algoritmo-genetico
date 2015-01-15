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

    @staticmethod    
    def aplicarCondicao(populacao, valorEsperado, quantidadeIndividuos):
        sum = 0
        contSatisf = 0
        contNotSatisf = 0        
        try:
            for candidato in populacao:    
                if candidato.avaliacao >= valorEsperado:
                    candidato.satisfazCondicao = True
                    contSatisf = contSatisf + 1
                else:
                    candidato.satisfazCondicao = False
                    contNotSatisf = contNotSatisf + 1
            if contSatisf <= quantidadeIndividuos & contSatisf != 0:
                return False
            else:
                return True
        except Exception as ex:
            print("Ocorreu o erro: {0} ".format(ex.args))

    @staticmethod    
    def selecionar(populacao, totalIndividuos, totalGene, quantidadeIndividuos):
        soma = 0
        cont = 0
        valorApPerc = 0
        try:
            for candidato in populacao:    
               soma = soma + candidato.avaliacao

            while True:
              cont = 0
              valorApPerc = 0
              for candidato in populacao:
                  r = rand.randint(1, soma)
                  valorApPerc = valorApPerc + candidato.avaliacao
                  if valorApPerc >= r:
                      candidato.selecionado = True
                      cont = cont + 1
                  else:
                      candidato.selecionado = False  
              if (cont % 2 != 0) or (cont < quantidadeIndividuos):
                break
        except Exception as ex:
            print("Ocorreu o erro: {0} ".format(ex.args))
