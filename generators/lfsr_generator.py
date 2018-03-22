from functools import reduce
from itertools import compress
from collections import Counter


def lfsr(polynomial):
    memory = [a for a in polynomial]
    while True:
        yield memory[0]
        memory = memory[1:] + [reduce(lambda a, x: a ^ x, compress(memory, polynomial))]


def voting_for_next_bit(values):
    return Counter(values).most_common(1)[0][0]


def choose_next_active(activation_flag, values):
    return [index for index, value in enumerate(values) if value == activation_flag]


def combine_lfsr(*polynomials):
    generators = [lfsr(polynomial) for polynomial in polynomials]
    values = [next(generator) for generator in generators]
    while True:
        bit = voting_for_next_bit(values)
        yield bit
        for index in choose_next_active(bit, values):
            values[index] = next(generators[index])
