class Cromossomo(object): 
    def __init__(self):
      self.__listaGene = list() 
      self.__nota = int()

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



