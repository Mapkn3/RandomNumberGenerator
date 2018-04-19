from functools import reduce
from itertools import compress, islice
from collections import Counter

from utils.converters import get_all_bin_combination


def calculate_max_t(polynomial):
    n = len(polynomial)
    polynomials = get_all_bin_combination(n)[1:]
    max_step = 0
    x = []
    for memory in polynomials:
        print(memory)
        generator = _lfsr(polynomial, [int(i) for i in memory])
        values = list(islice(generator, n+1))[n:]
        values_len = len(values)
        step = 0
        for i in generator:
            print(values)
            if values[:values_len//2] == values[values_len//2:]:
                break
            values.append(i)
            values_len = len(values)
            step += 1
        if step > max_step:
            max_step = step
            x = memory
    return [int(i) for i in x]


# LFSR генератор. Бесконечно возвращает сгенерированный бит из памяти. Инициализируется порождающим полиномом
def _lfsr(polynomial, init_memory):
    memory = init_memory
    while True:
        yield memory[0]
        memory = memory[1:] + [reduce(lambda a, x: a ^ x, compress(memory, polynomial))]


def lfsr(polynomial):
    return _lfsr(polynomial, calculate_max_t(polynomial))


# Мажоритарное голосование. Возвращает "популярный" бит.
def majority_vote(values):
    return Counter(values).most_common(1)[0][0]


# Возвращает список индексов генераторов, значение которых совпадает с требуемым значением(флаг активации)
def choose_next_active_generators(activation_flag, values):
    return [index for index, value in enumerate(values) if value == activation_flag]


# Комбинированый генератор с мажоритарным голосованием и неравномерным движением регистров.
# Принимает список порождающих полиномов. Возвращает сгенерированный и отобранный бит.
def combine_lfsr(*polynomials):
    generators = [lfsr(polynomial) for polynomial in polynomials]
    values = [next(generator) for generator in generators]
    while True:
        bit = majority_vote(values)
        yield bit
        for index in choose_next_active_generators(bit, values):
            values[index] = next(generators[index])


# Сохранение n бит в файл, которые сгенерированы с помощью генератора, переданного в параметрах.
def save_n_bits_to_file(generator, n, path_to_file):
    with open(path_to_file, 'w') as f:
        f.write(''.join(str(i) for i in islice(generator, n)))
