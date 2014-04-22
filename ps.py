from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


lista = [1,2,3,4,5,6,7,8,9,10]
a = set(lista)

x = list(powerset(a))
print list(x)

y = [sum(k) for k in powerset(a)]
print y

print zip(y,x)

impossiveis = sum(y)
print impossiveis

possiveis = set([sum(x) for x in powerset(a) if len(x) > 1])


if len(a.intersection(possiveis)) or list(sorted(lista)) != lista:
    print "This is not an A-sequence."
else:
    print "This is an A-sequence"

