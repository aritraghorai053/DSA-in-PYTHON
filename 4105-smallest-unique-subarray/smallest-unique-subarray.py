class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        base = 100003

        prefix = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            prefix[i + 1] = (prefix[i] * base + nums[i] + 1) % mod
            power[i + 1] = (power[i] * base) % mod

        def check(k):
            freq = {}

            for i in range(n - k + 1):
                h = (prefix[i + k] - prefix[i] * power[k]) % mod
                freq[h] = freq.get(h, 0) + 1

            return any(count == 1 for count in freq.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left