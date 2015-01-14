from random import Random
rand = Random()
class Gene:
    def __init__(self):
      self.__informacao =  rand.randint(1,9);

   
    @property
    def informacao(self):
        return self.__informacao


