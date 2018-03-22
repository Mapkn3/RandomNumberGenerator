from itertools import islice
from generators.lfsr_generator import combine_lfsr

random_number_generator = combine_lfsr([1, 0, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 0, 1, 1])

count_bits = 1_000_000
with open('mygen.txt', 'w') as f:
    f.write(''.join(str(i) for i in islice(random_number_generator, count_bits)))
