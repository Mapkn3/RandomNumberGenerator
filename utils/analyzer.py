from scipy import log

from utils.converters import get_all_bin_combination


# Дописывает m первых символов строки в конец и возвращает полученную строку
# 3, '10101' -> '10101101'
def append_m_beginning_char_to_end(m, string):
    return string + string[:m - 1]


# Считает количество вхождений подстроки в строку с пересечением
# '101', '1010101' -> 3
def count_pattern_in_string(pattern, string):
    n = len(string)
    m = len(pattern)
    target = append_m_beginning_char_to_end(m, string)
    all_m_pattern = [target[i:i + m] for i in range(n)]
    return all_m_pattern.count(pattern)


# Частоты встречи подстрок в строке. Возвращает список частот для переданного списка подстрок
# ['10', '01'], '101011' -> [0.5, 0.33333333333]
def hist_pattern_in_string(patterns, string):
    n = len(string)
    return [count_pattern_in_string(pattern, string) / n for pattern in patterns]


# Функция фи из англ книжки
def fi(values):
    return sum(map(lambda x: x * log(x), filter(lambda x: x > 0, values)))


# Функция апен из англ книжки
def apen(m, values):
    c_m = hist_pattern_in_string(get_all_bin_combination(m), values)
    c_m_plus_1 = hist_pattern_in_string(get_all_bin_combination(m + 1), values)
    print(f'For m = {m}')
    print(f'C_m = {c_m}')
    print(f'C_m+1 = {c_m_plus_1}')
    return fi(c_m) - fi(c_m_plus_1)


# Функция хи2 из англ книжки
def hi2(values, m):
    n = len(values)
    return 2 * n * (log(2) - apen(m, values))
