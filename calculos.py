# -*- coding: cp1252 -*-

#quanto tempo
anos = 35

#quantas progressoes (18 = p31 ateh p49)
progressoes = 18

#tempo das progressoes (em meses)
tprog = 18

#progressao atual
progatual = 0


#base salarial
base = 3666.54

#step
step = 0.038

#incentivo a qualificacao 1.52 mestrado
iq = 1.52


meses = 12
salarios = []


for cada in range(anos*meses):
    
    salario = base*iq

    if cada%tprog == 0 and progatual < progressoes:
        progatual += 1
        base = base + base*step

    salarios.append(salario)


print "%i salários, totalizando: R$%.2f"  % (len(salarios), sum(salarios))
print "Média dos 80%% maiores: R$%.2f" % ( sum(salarios[-int(len(salarios)*0.8):]) / (len(salarios)*0.8) )
