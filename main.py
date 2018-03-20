from functools import reduce
from itertools import compress
from collections import Counter

def LFSR(polynom):
    memory = [i for i in polynom]
    while True:
        yield memory[0]
        memory = memory[1:] + [reduce(lambda a, x: a^x, compress(memory, polynom))]

def combineLFSR(*polynoms):
    generators = [LFSR(polynom) for polynom in polynoms]
    values = [next(generator) for generator in generators]
    while True:
        value = sorted(dict(Counter(values)).items(), key=lambda i: i[1])[-1][0]
        yield value
        for i in range(len(values)):
            if values[i] == value:
                values[i] = next(generators[i])
        
randomGenerator = combineLFSR([1,0,0,1,0], [1,1,1,1,1], [1,0,0,1,1])
for i in randomGenerator:
    print(i)
