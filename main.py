from generators.lfsr_generator import combine_lfsr, save_n_bits_to_file
from statistic_tests import spectral_test, approximate_entropy_test, random_excursions_variant_test

random_number_generator = combine_lfsr([1, 0, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 0, 1, 1])

count_bits = 1_000_000
filepath = 'D:\zzz\__STUD__\Crypto\ЛР2\data.e'  # 'mygen.txt'

save_n_bits_to_file(random_number_generator, count_bits, filepath)
# print(spectral_test.test_values_from_file(filepath))
# print(approximate_entropy_test.test_values_from_file(10, filepath))
# print(random_excursions_variant_test.test_values_from_file(filepath))
