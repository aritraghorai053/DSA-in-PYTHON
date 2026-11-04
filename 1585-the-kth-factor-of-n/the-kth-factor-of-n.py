
from math import sqrt

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                small.append(i)

                if i != n // i:
                    large.append(n // i)

        factors = small + large[::-1]

        if k <= len(factors):
            return factors[k - 1]

        return -1
