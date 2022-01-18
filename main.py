import numpy
import numpy as np
from scipy.special import factorial
from math import comb

def multinom(c):
    c = np.array(c)
    return int(factorial(c.sum()) / factorial(c).prod())

def main():
    m = 8
    assert m >= 4
    print(f'm**4= {m ** 4}')

    s2 = multinom([4]) * m  # one of the k_i is 4, rest are 0
    s2 += multinom([3, 1]) * comb(m, 2) * 2 # one of the k_i is 3, another k_i is 1, rest are 0
    s2 += multinom([2, 2]) * comb(m, 2)  # two of the k_i is 2, rest are 0
    s2 += multinom([1, 1, 2]) * comb(m, 3) * 3 # two of the k_i are 1, another is 2, rest are 0
    s2 += multinom([1, 1, 1, 1]) * comb(m, 4)   # 4 of the k_i's are 1,  rest are 0

    print(f'sum of counts = {s2}')


if __name__ == '__main__':
    main()
