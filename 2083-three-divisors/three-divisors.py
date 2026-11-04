class Solution:
    def isThree(self, n: int) -> bool:
        count = 0

        for i in range (1, int(sqrt(n))+1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1

        return count == 3