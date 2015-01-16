class Cromossomo(object): 
    def __init__(self):
      self.__listaGene = list() 
      self.__nota = int()
      self.__satisfazCondicao = False
      self.__selecionado = False

    @property
    def avaliacao(self):
        return self.__nota

    @avaliacao.setter
    def avaliacao(self, nota):
        self.__nota = nota
    
    @property
    def listaGene(self):
        return self.__listaGene

    @listaGene.setter
    def listaGene(self, listaGene):
        self.__listaGene = listaGene

    @property
    def satisfazCondicao(self):
        return self.__satisfazCondicao

    @satisfazCondicao.setter
    def satisfazCondicao(self, satisfazCondicao):
        self.__satisfazCondicao = satisfazCondicao

    @property
    def selecionado(self):
        return self.__selecionado

    @selecionado.setter
    def selecionado(self, selecionado):
        self.__selecionado = selecionado
    


