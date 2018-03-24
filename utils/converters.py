def bit_string_to_bit_list(bit_string):
    return [int(i) for i in bit_string]


def normalized_sequence(sequence):
    return list(map(lambda x: 2 * x - 1, sequence))


def get_all_bin_combination(m):
    return [f'{i:0{m}b}' for i in range(2 ** m)]
