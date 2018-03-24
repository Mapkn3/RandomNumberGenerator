from scipy import log
from scipy.special import gammaincc

from utils.analyzer import hist_pattern_in_string
from utils.converters import get_all_bin_combination


def fi(values):
    return sum(map(lambda x: x * log(x), filter(lambda x: x > 0, values)))


def apen(m, values):
    print(f'For m = {m}')
    c_m = hist_pattern_in_string(get_all_bin_combination(m), values)
    print(f'C_m = {c_m}')
    c_m_plus_1 = hist_pattern_in_string(get_all_bin_combination(m + 1), values)
    print(f'C_m+1 = {c_m_plus_1}')
    return fi(c_m) - fi(c_m_plus_1)


def hi2(values, m):
    n = len(values)
    return 2 * n * (log(2) - apen(m, values))


def approximate_entropy(values):
    m = 3
    hi = hi2(values, m)
    print(f'X2 = {hi}')
    p_value = gammaincc(2 ** (m - 1), hi / 2)
    print(f'p_value = {p_value}')
    return p_value > 0.01


def test_values_from_file(path_to_file):
    with open(path_to_file, 'r') as f:
        return approximate_entropy(f.read())
