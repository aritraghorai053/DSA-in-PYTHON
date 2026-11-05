class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        ans = [1, num + 1]
        diff = num
        for n in [num + 1, num + 2]:
            for i in range(int(sqrt(n)), 0, -1):
                if n % i == 0:
                    d = n // i - i


                    if d < diff:
                        diff = d
                        ans = [i, n // i]

                    break

        return ans
