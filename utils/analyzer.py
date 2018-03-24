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