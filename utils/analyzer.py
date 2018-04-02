from scipy import log

from utils.converters import get_all_bin_combination


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
    c_m = hist_pattern_in_string(get_all_bin_combination(m), values)
    c_m_plus_1 = hist_pattern_in_string(get_all_bin_combination(m + 1), values)
    print(f'For m = {m}')
    print(f'C_m = {c_m}')
    print(f'C_m+1 = {c_m_plus_1}')
    return fi(c_m) - fi(c_m_plus_1)


def hi2(values, m):
    n = len(values)
    return 2 * n * (log(2) - apen(m, values))
