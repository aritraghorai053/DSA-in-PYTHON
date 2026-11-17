class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        indices = list(range(i + r, j + 1, d))

                        l, h = 0, len(indices) - 1

                        while l < h:
                            if s[indices[l]] != s[indices[h]]:
                                changes += 1
                            l += 1
                            h -= 1

                    cost[i][j] = min(cost[i][j], changes)

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for j in range(i):
                    if i - j < 2:
                        continue

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[j][parts - 1] + cost[j][i - 1]
                    )

        return dp[n][k]