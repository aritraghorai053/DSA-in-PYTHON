import heapq

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:

        n = len(nums)
        INF = float('inf')

        small = []  # Max heap (lower half)
        large = []  # Min heap (upper half)

        delayed = {}
        small_size = 0
        large_size = 0
        small_sum = 0
        large_sum = 0

        def prune(heap):
            while heap:
                val = -heap[0] if heap == small else heap[0]

                if delayed.get(val, 0):
                    heapq.heappop(heap)
                    delayed[val] -= 1

                    if delayed[val] == 0:
                        del delayed[val]
                else:
                    break

        def balance():
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            if small_size > large_size + 1:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)

                small_size -= 1
                large_size += 1

                small_sum -= val
                large_sum += val

                prune(small)

            elif small_size < large_size:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)

                small_size += 1
                large_size -= 1

                small_sum += val
                large_sum -= val

                prune(large)

        def add(val):
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            if not small or val <= -small[0]:
                heapq.heappush(small, -val)
                small_size += 1
                small_sum += val
            else:
                heapq.heappush(large, val)
                large_size += 1
                large_sum += val

            balance()

        def remove(val):
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            delayed[val] = delayed.get(val, 0) + 1

            if val <= -small[0]:
                small_size -= 1
                small_sum -= val

                if val == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                large_sum -= val

                if large and val == large[0]:
                    prune(large)

            balance()

        # Calculate the minimum cost for every window of size x.
        costs = []

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                median = -small[0]

                cost = (median * small_size - small_sum) + \
                       (large_sum - median * large_size)

                costs.append(cost)

        # DP: minimum cost to select j non-overlapping windows
        # within the first i elements.
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    cost = costs[i - x]

                    curr[i] = min(
                        curr[i],
                        prev[i - x] + cost
                    )

            prev = curr

        return prev[n]