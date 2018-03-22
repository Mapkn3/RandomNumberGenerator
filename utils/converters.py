def bit_string_to_bit_list(bit_string):
    return [int(i) for i in bit_string]


def normalized_sequence(sequence):
    return list(map(lambda x: 2 * x - 1, sequence))
