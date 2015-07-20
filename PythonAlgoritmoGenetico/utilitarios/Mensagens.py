class Mensagens(object):
   def __init__(self):
      self.__mensagem  = {
        #PhytonAlgoritmoGenerito.py---------------------------------------------------------------------------
        'nome.programa' : "SUGEST\u00C7\u00D5ES DE COMPET\u00CANCIAS PARA O CARGO DE [Coordenador de Recursos Humanos]",
        'insira.quantidade.individuos' : "\n 1. Insira a quantidade de candidatos para serem gerados aleat\u00F3riamente: ",
        'inserir.valor.minimo.individuos' : "\n 2. Insira o valor m\u00EDnimo para a sele\u00E7\u00E3o de candidatos: ",
        'inserir.quantidade.maxima.obter.individuos' : "\n 3. Insira a quantidade m\u00E1xima de candidatos que se deseja obter: ",
        'cabecalho.configuracoes.programa' : "\n ===================== CONFIGURA\u00C7\u00D5ES DO PROGRAMA ===================== ",
        'rodape.configuracoes.programa' : "\n ===================================================================== ",
        'total.individuos' : "\n Total de candidatos: {0}",
        'valor.minimo.selecao.individuos': "\n Valor m\u00EDnimo para a sele\u00E7\u00E3o de candidatos: {0} ",
        'quantidade.minima.individuos' : "\n Quantidade  m\u00EDnima de candidatos que se deseja obter : {0} ",
        'total.criterio.de.avaliacao.padrao' : "\n [Padr\u00E3o/Programa] Total de crit\u00E9rios de avalia\u00E7\u00E3o : {0} ",
        'mensagem.gerando.candidatos' : " \n\n Gerando candidatos ... \n\n" ,
        'mensagem.avaliando.candidatos' : " \n\n Avaliando candidatos ... \n\n"
        #-------------------------------------------------------------------------------------------------------
      }

   @property
   def mensagem(self):
        return self.__mensagem

  




