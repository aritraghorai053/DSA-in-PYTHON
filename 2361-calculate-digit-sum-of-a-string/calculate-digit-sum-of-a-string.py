class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]
                total = 0

                for ch in group:
                    total += int(ch)

                res += str(total)

            s = res

        return s
        