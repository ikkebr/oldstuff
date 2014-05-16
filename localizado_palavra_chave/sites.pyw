# -*- coding: cp1252 -*-
from __future__ import unicode_literals
import htmllib, formatter
import urllib2, htmllib, formatter
from urlparse import urljoin
import multiprocessing
from multiprocessing import Pool, Process
from Queue import Queue, Empty
from threading import Thread
import webbrowser
import HTMLParser


#palavra a ser procuprada
#palavra = raw_input("Digite a palavra ou frase a ser encontrada: ")
palavra = open("palavra.txt","r")
palavra = unicode(palavra.readlines()[0].decode('iso8859-1'))

#print palavra


lista = open("lista.txt","r")
lista = lista.readlines()

#lista de sites
#entre aspas e com uma virgula no final
#lista = []


if palavra == u"Tânia":
   print u"Tânia"


class LinksExtractor(htmllib.HTMLParser):

   def __init__(self, formatter, base):
      htmllib.HTMLParser.__init__(self, formatter)
      self.links = []
      self.base = base

   def start_a(self, attrs):
      if len(attrs) > 0 :
         for attr in attrs :
            if attr[0] == "href" and "javascript" not in attr[1] and attr[1] != "#" and attr[1] not in self.links:
                if "http://" not in attr[1]:
                    self.links.append(urljoin(self.base, attr[1]))
                else:
                    self.links.append(attr[1])

   def get_links(self):
      return self.links


queue = Queue()

def navegar():
   try:
      while True:
         cada = queue.get_nowait()
         print '.',
         try:
            site = urllib2.urlopen(cada, timeout=5)
            conteudo = site.read()
            x = HTMLParser.HTMLParser()
            conteudo = x.unescape(conteudo.decode('iso8859-1'))
   
            if palavra in conteudo:
               print ""
               print cada
               
         except Exception, err:
            #print Exception, err
            pass
   except Empty:
      pass

   return navegar
   

print "EXECUTANDO..."

#first level
for cada in lista:

    try:
        site = urllib2.urlopen(cada, timeout=10)
        conteudo = site.read()

        format = formatter.NullFormatter()
        htmlparser = LinksExtractor(format, site.url)
        htmlparser.feed(conteudo)
        htmlparser.close()

        links = htmlparser.get_links()
        for link in links:
           queue.put(link)
                   
        if palavra in conteudo:
           print site.url

    except:
        pass

workers = []
for i in range(5):
   worker = Thread(target=navegar)
   worker.start()
   workers.append(worker)

   for worker in workers:
      worker.join()


raw_input("Pressione ENTER para encerrar")
