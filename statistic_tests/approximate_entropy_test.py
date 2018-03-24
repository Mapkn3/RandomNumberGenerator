from scipy import log
from scipy.special import gammaincc


def get_all_bin_combination(m):
    return [f'{i:0{m}b}' for i in range(2 ** m)]


def append_m_beginning_char_to_end(m, string):
    return string + string[:m - 1]


def count_pattern_in_string(pattern, string):
    n = len(string)
    m = len(pattern)
    target = append_m_beginning_char_to_end(m, string)
    all_m_pattern = [target[i:i + m] for i in range(n)]
    return all_m_pattern.count(pattern)


def hist_pattern_in_string(patterns, string):
    n = len(string)
    return [count_pattern_in_string(pattern, string) / n for pattern in patterns]


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
