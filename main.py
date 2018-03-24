from itertools import islice
from generators.lfsr_generator import combine_lfsr
from statistic_tests import spectral_test, approximate_entropy_test

random_number_generator = combine_lfsr([1, 0, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 0, 1, 1])

count_bits = 1_000_000
filepath = 'mygen.txt'
with open('mygen.txt', 'w') as f:
    f.write(''.join(str(i) for i in islice(random_number_generator, count_bits)))

print(spectral_test.test_values_from_file(filepath))
print(approximate_entropy_test.test_values_from_file(filepath))
