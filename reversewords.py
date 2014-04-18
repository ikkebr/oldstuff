from itertools import permutations
while True:
    try:
        test = raw_input()
        print  ",".join(sorted(["".join(x) for x in list(permutations(test))]))
    except:
        pass
