from random import randint
from pprint import pprint
from copy import deepcopy

NORTE = 0
SUL = 1
ESQUERDA = 2
DIREITA = 3



#labirinto = [list('---#--'),
             #list('-#-##-'),
             #list('-###-#'),
             #list('---#--'),
             #list('##--#-'),
             #list('--#---')]

#labirinto = [list('-#---#---#'),
             #list('-#-#-###-#'),
             #list('---#-----#'),
             #list('#####-####'),
             #list('#-###-#--#'),
             #list('#-#---##-#'),
             #list('--###-##--'),
             #list('#-------#-'),
             #list('#####-###-'),
             #list('#---------')]

             
labirinto = [list('-##-#-###-######-###'),
             list('-##-#-----######-#-#'),
             list('------###--------#-#'),
             list('###########-######-#'),
             list('#------------------#'),
             list('########-#########--'),
             list('---------#-----#-#-#'),
             list('########-#-#####-#-#'),
             list('-#-----###-#-------#'),
             list('-#-#-#-----#-####-##'),
             list('-#-#-#####---------#'),
             list('-##########-####-#-#'),
             list('------##########-#-#'),
             list('-###-##--------#-#-#'),
             list('-#---###-#####-#-###'),
             list('-#########-#-#-#---#'),
             list('-----------------#-#'),
             list('##################-#')]

def formata_labirinto(labirinto):
    return "\n".join(" ".join(cada) for cada in labirinto)


def posicao(labirinto):
    while True:
        x = randint(0,len(labirinto)-1)
        y = randint(0,len(labirinto[0])-1)
        
        if labirinto[x][y] == '-':
            return (x,y)


original = deepcopy(labirinto)


entrada = posicao(labirinto)
saida = posicao(labirinto)




#verifica se dah pra ir
def pode_ir(x,y,direcao):
    try:
        if direcao == 0:
            if x-1 >= 0: #index negativo do python funciona, tem que matar.
                return True if labirinto[x-1][y] == '-' else False
        elif direcao == 1:
            return True if labirinto[x+1][y] == '-' else False
        elif direcao == 2:
            if y-1 >= 0: #index negativo do python funciona, tem que matar.
                return True if labirinto[x][y-1] == '-' else False
        elif direcao == 3:
            return True if labirinto[x][y+1] == '-' else False
    except:
        pass
    return False



pintou = True
#mata os caminhos que nao podem ser ^^
while pintou:
    pintou = False
    for x in range(len(labirinto)):
        for y in range(len(labirinto[0])):
            if len([True for direcao in range(4) if pode_ir(x,y,direcao)]) < 2 and (x,y) != entrada and (x,y) != saida and labirinto[x][y] == '-':
                labirinto[x][y] = '@'
                pintou = True    

#pprint(labirinto) #segredo



def caminhar(atual, lista):
    x,y = atual
    
    if atual == saida:
        return (True, lista+[(x,y)])
    
    #cima
    if pode_ir(x,y, 0) and (x-1, y) not in lista:
        sit, caminho = caminhar((x-1, y), lista[::]+[(x,y)])
        if sit:
            return (sit, caminho)
        
    #baixo
    if pode_ir(x,y, 1) and (x+1,y) not in lista:
        sit, caminho = caminhar((x+1, y), lista[::]+[(x,y)])
        if sit:
            return (sit, caminho)
    
    #direita
    if pode_ir(x,y, 3) and (x, y+1) not in lista:
        sit, caminho = caminhar((x,y+1), lista[::]+[(x,y)])
        if sit:
            return (sit, caminho)
        
    #esquerda
    if pode_ir(x,y, 2) and (x, y-1) not in lista:
        sit, caminho = caminhar((x,y-1), lista[::]+[(x,y)])
        if sit:
            return (sit, caminho)
        
    return (False, lista)


mudar = caminhar(entrada, [])[1]

posicao = list(entrada)

original[entrada[0]][entrada[1]] = 'E'
original[saida[0]][saida[1]] = 'S'

print "Labirinto Normal"
#pprint(original)
print formata_labirinto(original)
raw_input("Pressione enter")

print "Com Dead-End-Filling"
print formata_labirinto(labirinto)
raw_input("Pressione enter")



raw_input()
print "Caminhando"

for (x,y) in mudar:
    original[x][y] = 'x'
    print formata_labirinto(original)
    print '\n'
    raw_input()

print formata_labirinto(original)
