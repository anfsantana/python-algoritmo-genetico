class Candidato(object):
    def __init__(self):
      self.__listaCandidatos = list() 

    @property
    def listaCandidatos(self):
        return self.__listaCandidatos

    @listaCandidatos.setter
    def listaCandidatos(self, listaCandidatos):
        self.__listaCandidatos = listaCandidatos
    



