fibs = {0: 0, 1: 1}
def fast_fib(n):
    if n in fibs: return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fast_fib((n / 2) - 1)) + fast_fib(n / 2)) * fast_fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fast_fib((n - 1) / 2) ** 2) + (fast_fib((n+1) / 2) ** 2)
        return fibs[n]


#print fast_fib(30000)
