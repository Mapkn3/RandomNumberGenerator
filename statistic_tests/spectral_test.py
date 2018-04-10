from scipy import sqrt, log
from scipy.fftpack import fft
from scipy.special import erfc

from utils.converters import bit_string_to_bit_list, normalized_sequence


# Спектральный тест по англ книжке
def spectral(values):
    bit_list = bit_string_to_bit_list(values)
    signal = normalized_sequence(bit_list)
    n = len(signal)
    s = abs(fft(signal))
    s_div_2 = s[:n // 2]
    t = sqrt(log(1 / 0.05) * n)
    n0 = (0.95 * n) / 2
    n1 = len(list(filter(lambda x: 0 < x < t, s_div_2)))
    d = (n1 - n0) / sqrt((n * 0.95 * 0.05) / 4)
    p_value = erfc(abs(d) / sqrt(2))

    print(f'signal = {signal}')
    print(f'n = {n}')
    print(f's = {s}')
    print(f's_div_2 = {s_div_2}')
    print(f't = {t}')
    print(f'n0 = {n0}')
    print(f'n1 = {n1}')
    print(f'd = {d}')
    print(f'p_value = {p_value}')
    return p_value > 0.01


# Тест битов из файла
def test_values_from_file(path_to_file):
    with open(path_to_file, 'r') as f:
        return spectral(f.read())
