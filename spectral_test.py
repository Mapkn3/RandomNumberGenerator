from math import sqrt, log
from scipy.fftpack import fft
from scipy.special import erfc


def bit_string_to_bit_list(str):
    return [int(i) for i in str]


def spectral(values):
    signal = list(map(lambda x: 2*x-1, values))
    print(f'signal = {signal}')
    n = len(signal)
    print(f'n = {n}')
    s = abs(fft(signal))
    print(f's = {s}')
    s2 = s[:n//2]
    print(f's2 = {s2}')
    t = sqrt(log(1/0.05)*n)
    print(f't = {t}')
    n0 = (0.95*n)/2
    print(f'n0 = {n0}')
    n1 = len(list(filter(lambda x: x < t, s2)))-1
    print(f'n1 = {n1}')
    d = (n1-n0)/sqrt((n*0.95*0.05)/4)
    print(f'd = {d}')
    p_value = erfc(abs(d)/sqrt(2))
    return p_value
    

print(spectral(bit_string_to_bit_list('1001010011')))
