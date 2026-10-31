
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0, 0] for _ in range(n + 1)]
        dp[1] = [1, 1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j + 1] = [dp[j + 1][1], dp[j][0]]
                else:
                    val = (dp[j][0] + dp[j + 1][1]) % MOD
                    dp[j + 1] = [val, val]

        return dp[n][0]
