class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        

        result = 0

        for i in range(1, n+1):
            if n % i == 0:
                result += 1
                if result == k:
                    return i

        return -1