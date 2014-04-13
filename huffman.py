# -*- coding: cp1252 -*-
from __future__ import division
import sys
from operator import itemgetter

## USO: python huffman.py "texto a ser codificado"
##Arvore de Huffman em Python
##Henrique Gabriel Gularte Pereira
##12 de Agosto de 2008
class arvoreHuffman(object):

##
##        Nodo generico
##   
    class nodo(object):
        def __init__(self, fesq = None, fdir = None, valor = None, desc=None):
            self.descricao = desc
            self.fesq = fesq
            self.fdir = fdir
            self.valor = valor

    
##  Construtor da Arvore de Huffman
##  texto = mensagem a ser codificada
##  insensivel = avaliando o texto como case insensitive    
    def __init__(self, texto = "Teste da arvore do huffman", insensivel = True):

        if insensivel:
            texto = texto.lower()
        self.texto = texto    
        self.frequencia = self.pegaFrequencia(texto)
        self.criaNodos()
        self.estrutura = self.geraArvore()
        self.dicionario = {}
        self.caminhaArvore(self.tfreq[0][2],"")
        #supondo que cada letra da mensagem seja codificada em 8 bits
        self.tamanhooriginal = len(texto)*8

        #utilizando nosso dicionario de codificacao
        self.tamanhonovo = sum( [len(self.dicionario[x]) for x in self.texto] )

##  Metodo que imprime os resultados da classe
    def __str__(self):
        retorno  = "O texto era: %s\n" % self.texto
        retorno += "Supondo que cada letra fosse codificada em 8 bits o tamanho seria %i bits\n" % self.tamanhooriginal
        retorno += "Codificando cada letra em uma arvore de Huffman temos:\nCaract.\t\tRepresentacao\t\t\tFrequencia\n"
        for x in self.codificacao():
            retorno += "%s\t\t%s\t\t\t\t%i\n" % (x[0],x[1], self.dfrec[x[0]])
            #dictdomal[x[1]] = x[0]

        retorno += "\nO tamanho da mensagem codificada ficou %i bits\n" % self.tamanhonovo
        retorno += "Ocorreu uma economia de %f" % (100-self.tamanhonovo/self.tamanhooriginal*100)
        retorno += "% " + "no tamanho da mensagem\n" 
        retorno += "\nA mensagem codificada ficou: %s\n" % self.codificado()
        global msgcod
        msgcod = self.codificado()

        return retorno

##  Metodo que calcula a frequencia de cada letra
##  dentro de um texto e retorna uma lista ordenada
##  por frequencia - formato: ('letra',frequencia)
    def pegaFrequencia(self, texto):
        contagem = {}
        for letra in texto:
            if letra in contagem:
                contagem[letra]+= 1
            else:
                contagem[letra] = 1
        self.dfrec = contagem
        return sorted(contagem.iteritems(), key=itemgetter(1), reverse=True)

##  Vasculha a lista de frequencias e gera um nodo
##  para cada entrada na lista
    def criaNodos(self):
        self.tfreq = []
        for tupla in self.frequencia:
            self.tfreq.append( (tupla[0], tupla[1], arvoreHuffman.nodo(valor = tupla[0])) )

##  Depois da criacao da lista com os nodos basicos
##  executa o algoritimo de criacao da arvore de Huffman
    def geraArvore(self):
        #print self.tfreq
        while len(self.tfreq) > 1:
            valordir = self.tfreq.pop() # direita pega o menor
            valoresq = self.tfreq.pop() # esquerda pega o segundo menor
            nodoesq = valoresq[2] #pega nodo esquerda
            nododir = valordir[2] #pega nodo direita
            novonodo = arvoreHuffman.nodo(fesq = nodoesq, fdir= nododir) # cria o nodo da juncao dos dois nodos

            self.tfreq.append( ("%s+%s" % (valoresq[0], valordir[0]), valoresq[1]+valordir[1], novonodo) ) # adiciona na lista de frequencias e nodos
            self.tfreq = sorted(self.tfreq, key=itemgetter(1), reverse=True) # reordena a lista

        return self.tfreq

## Funcao que gera o dicionario de decodificacao
## caminha toda a arvore e adiciona em um dicionario
## a codificacao equivalente a cada letra
    def caminhaArvore(self, nodo, bstring):
        if nodo.fesq is not None:
            self.caminhaArvore(nodo.fesq, bstring+"0")

        if nodo.fdir is not None:
            self.caminhaArvore(nodo.fdir, bstring+"1")

        if nodo.valor is not None:
            self.dicionario[nodo.valor] = bstring

        pass

## retorna uma lista de tuplas com a codificacao
## ordenado lexicamente no formato ('letra','codificacao')
    def codificacao(self):
        return sorted(self.dicionario.iteritems(), key=itemgetter(0))

## retorna a mensagem codificada
    def codificado(self):
        return "".join([self.dicionario[x] for x in self.texto])


    def descomprime(self):
        strinicio = 0
        strfim = 1
        msg = ""
        msgcod = self.codificado()
        dictchave = {}

        #cria um dicionario onde as chaves sao os valores codificados
        #e os valores sao as letras que serao exibidas na tela
        for chave, valor in list(self.dicionario.iteritems()):
            dictchave[valor] = chave

        #print dictchave

        #percore toda a string codificada, verificando se existe no
        #dicionario uma chave com valor igual a string lida, caso
        #exista, adiciona na mensagem, caso nao exista, aumenta mais
        #uma casa na string e tenta novamente
        while strfim <= len(msgcod):
            try:
                #print msgcod[strinicio:strfim]
                msg += dictchave[msgcod[strinicio:strfim]]
                strinicio = strfim
                strfim += 1
            except:
                #print msg
                strfim += 1

        return msg


if len(sys.argv) < 2:
    arvore = arvoreHuffman("Oloco meu! Mataram alguém")
   
else:
    arvore = arvoreHuffman(" ".join(sys.argv[1:]))
    
print arvore
print arvore.descomprime()






    
