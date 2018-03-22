def get_all_bin_combination(m):
    return [f'{i:0{m}b}' for i in range(2**m)]


def count_pattern_in_string(pattern, string):
    n = len(string)
    m = len(pattern)
    target = string + string[:m-1]
    all_m_pattern = [target[i:i + m] for i in range(n)]
    return all_m_pattern.count(pattern)


for pattern in get_all_bin_combination(3):
    print(count_pattern_in_string(pattern, '110101011000100'))
