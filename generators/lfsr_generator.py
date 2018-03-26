from functools import reduce
from itertools import compress, islice
from collections import Counter


def lfsr(polynomial):
    memory = [a for a in polynomial]
    while True:
        yield memory[0]
        memory = memory[1:] + [reduce(lambda a, x: a ^ x, compress(memory, polynomial))]


def majority_vote(values):
    return Counter(values).most_common(1)[0][0]


def choose_next_active_generators(activation_flag, values):
    return [index for index, value in enumerate(values) if value == activation_flag]


def combine_lfsr(*polynomials):
    generators = [lfsr(polynomial) for polynomial in polynomials]
    values = [next(generator) for generator in generators]
    while True:
        bit = majority_vote(values)
        yield bit
        for index in choose_next_active_generators(bit, values):
            values[index] = next(generators[index])


def save_n_bits_to_file(generator, n, path_to_file):
    with open(path_to_file, 'w') as f:
        f.write(''.join(str(i) for i in islice(generator, n)))
