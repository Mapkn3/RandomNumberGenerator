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
        value = Counter(values).most_common(1)[0][0]
        yield value
#        for ind, val in enumerate(values):
#            if val == value
#                values[ind] = next(generators[ind])

#        values = [next(generators[ind]) if val == value else val for ind, val in enumerate(values)]

#        for i in range(len(values)):
#            if values[i] == value:
#                values[i] = next(generators[i])
        
randomGenerator = combineLFSR([1,0,0,1,0], [1,1,1,1,1], [1,0,0,1,1])
for i in randomGenerator:
    print(i)

