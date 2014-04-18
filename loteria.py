from __future__ import division
from math import factorial, ceil, floor

def fac(a,b):
    try:
        if a == b:
            return 1
        else:
            return factorial(a)/(factorial(a-b)*factorial(b))
    except:
        return 0
    
def loteria(m,n,t,p):
    '''
    >>> loteria(100, 10, 2, 1)
    '0.1000000000'

    >>> loteria(100, 10, 2, 2)
    '0.1909090909'

    >>> loteria(10,10,5,1)
    '1.0000000000'


    >>> loteria(100, 10, 1, 2)
    '0.0090909091'

    >>> loteria(100, 10, 1, 1)
    '0.1000000000'

    >>> loteria(100, 10, 1, 11)
    '0.0000000000'

    >>> loteria(10, 10, 1, 1)
    '1.0000000000'

    >>> loteria(10, 10, 1, 2)
    '1.0000000000'


    >>> loteria(10, 10, 2, 2)
    '1.0000000000'

    >>> loteria(10, 9, 2, 2)
    '1.0000000000'

    >>> loteria(10, 2, 2, 1)
    '0.2000000000'
    
    '''
    K = ceil(p/t)
    t = fac(m, n)
    #return int(K)
    return "%.10f" % sum([(fac(p, K) * fac((m-p), (n - K)))/t for K in range(int(K), p+1)])



if __name__== "__main__":
    m,n,t,p = map(int, raw_input().split(' '))
    print loteria(m,n,t,p)
