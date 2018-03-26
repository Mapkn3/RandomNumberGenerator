from scipy.special import gammaincc

from utils.analyzer import hi2


def approximate_entropy(m, values):
    hi = hi2(values, m)
    print(f'X2 = {hi}')
    p_value = gammaincc(2 ** (m - 1), hi / 2)
    print(f'p_value = {p_value}')
    return p_value > 0.01


def test_values_from_file(m, path_to_file):
    with open(path_to_file, 'r') as f:
        return approximate_entropy(m, f.read())
