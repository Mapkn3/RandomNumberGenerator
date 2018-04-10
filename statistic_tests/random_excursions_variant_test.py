from collections import Counter
from itertools import accumulate

from scipy import sqrt
from scipy.special import erfc

from utils.converters import bit_string_to_bit_list, normalized_sequence


# Тест произвольных отклонений (вар. 2) по англ книжке
def random_excursions_variant(values):
    bit_list = bit_string_to_bit_list(values)
    signal = normalized_sequence(bit_list)
    s = list(accumulate(signal))
    s0 = [0] + s + [0]
    z = Counter(s0)
    j = z[0] - 1
    x = [i for i in range(-9, 10) if i]
    p_values = [erfc(abs(z[i] - j) / sqrt(2 * j * (4 * abs(i) - 2))) for i in x]
    result = [(i, p_values[i] >= 0.01) for i in x]
    print(f'signal={signal}')
    print(f's={s}')
    print(f's0={s0}')
    print(f'z={z}')
    print(f'j={j}')
    print(f'x={x}')
    print(f'p_values={p_values}')
    print(f'result={result}')
    return result


# Тест битов из файла
def test_values_from_file(path_to_file):
    with open(path_to_file, 'r') as f:
        return random_excursions_variant(f.read())
