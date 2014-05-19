def lower_if_possible(x):
    try:
        return x[0].lower()
    except AttributeError:
        return x


palavras = open("palavras.txt", "r");

palavras_lidas = palavras.read()
palavras_lidas = palavras_lidas.replace('\n','')
palavras_lidas = palavras_lidas.replace('\t','')
palavras_lidas = palavras_lidas.replace('(','').replace(')','').replace(';','').replace('+','').replace('-','')
palavras_lidas = palavras_lidas.replace('-','').replace(',','').replace(':','').replace('.','')

#conjunto_palavras = set(palavras_lidas.split())
lista_de_palavras = palavras_lidas.split()
lista_de_palavras.sort(key=lambda x: map(lower_if_possible,x))
novas_palavras = lista_de_palavras
#novas_palavras = sorted(palavras_lidas.split())


nova_lista = open("nova.txt", "w")
for cada in novas_palavras:
    if len(cada) > 2:
        nova_lista.write("%s\n" % cada)


nova_lista.close()


conjunto_palavras = set(palavras_lidas.split())
novas_palavras = sorted(conjunto_palavras)
nova_lista = open("nova_unica.txt", "w")

for cada in novas_palavras:
    if len(cada) > 2:
        nova_lista.write("%s\n" % cada)

nova_lista.close()
