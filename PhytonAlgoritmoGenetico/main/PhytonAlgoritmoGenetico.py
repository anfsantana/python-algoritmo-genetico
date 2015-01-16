from Genetico import Genetico
from Cromossomo import Cromossomo
from Gene import Gene
from Mensagens import Mensagens
import time
import os

msg = Mensagens()
totalGene = 7

print(msg.mensagem['nome.programa'])

totalIndividuos = input(msg.mensagem['insira.quantidade.individuos'])
valorEsperado =   input(msg.mensagem['inserir.valor.minimo.individuos'])
quantidadeIndividuos = input(msg.mensagem['inserir.quantidade.maxima.obter.individuos'])

os.system("cls")
print(msg.mensagem['nome.programa'])
print(msg.mensagem['cabecalho.configuracoes.programa'])
print(msg.mensagem['total.individuos'].format(totalIndividuos))
print(msg.mensagem['valor.minimo.selecao.individuos'].format(valorEsperado))
print(msg.mensagem['quantidade.minima.individuos'].format(quantidadeIndividuos))
print(msg.mensagem['total.criterio.de.avaliacao.padrao'].format(totalGene));
print(msg.mensagem['rodape.configuracoes.programa'])

print (msg.mensagem['mensagem.gerando.candidatos'])
time.sleep(5)
candidatos = Genetico().gerarPopulacao(int(totalIndividuos), int(totalGene))
Genetico().listarCandidatos(candidatos.listaCandidatos)

print (msg.mensagem['mensagem.avaliando.candidatos'])
time.sleep(5)
Genetico().avaliar(candidatos.listaCandidatos)

#Descomentar e continuar fazendo ... Senão fica em loop infinito.
#while (Genetico().aplicarCondicao(candidatos.listaCandidatos, int(valorEsperado), int(quantidadeIndividuos))):
#       Genetico().selecionar(candidatos.listaCandidatos, int(totalIndividuos), int(totalGene), int(quantidadeIndividuos))