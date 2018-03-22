from math import sqrt, log
from scipy.fftpack import fft
from scipy.special import erfc
from utils.converters import bit_string_to_bit_list, normalized_sequence


def spectral(values):
    signal = normalized_sequence(values)
    print(f'signal = {signal}')
    n = len(signal)
    print(f'n = {n}')
    s = abs(fft(signal))
    print(f's = {s}')
    s_div_2 = s[:n // 2]
    print(f's_div_2 = {s_div_2}')
    t = sqrt(log(1 / 0.05) * n)
    print(f't = {t}')
    n0 = (0.95 * n) / 2
    print(f'n0 = {n0}')
    n1 = len(list(filter(lambda x: 0 < x < t, s_div_2)))
    print(f'n1 = {n1}')
    d = (n1 - n0) / sqrt((n * 0.95 * 0.05) / 4)
    print(f'd = {d}')
    p_value = erfc(abs(d) / sqrt(2))
    print(f'p_value = {p_value}')
    return p_value > 0.01


def test_values_from_file(path_to_file):
    with open(path_to_file, 'r') as f:
        return spectral(bit_string_to_bit_list(f.read()))
