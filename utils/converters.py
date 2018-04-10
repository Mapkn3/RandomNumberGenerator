# Преобразует строку из 0 и 1 в список 0 и 1
# '101' -> [1, 0, 1]
def bit_string_to_bit_list(bit_string):
    return [int(i) for i in bit_string]


# Преобразует список 0 и 1 в список -1 и 1 соответственно
# [1, 0, 1] -> [1, -1, 1]
def normalized_sequence(sequence):
    return list(map(lambda x: 2 * x - 1, sequence))


# Возвращает список всевозможных битовых строк длины m
# 2 -> ['00', '01', '10', '11']
def get_all_bin_combination(m):
    return [f'{i:0{m}b}' for i in range(2 ** m)]
